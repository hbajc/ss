import asyncio
import json
import numpy as np
import websockets
from wyoming.audio import AudioChunk
from wyoming.server import AsyncServer
from wyoming.stt import Transcript, StartListening, StopListening, Audio

SHERPA_WS_URL = "ws://localhost:6006"

class SherpaSTTSession:
    def __init__(self):
        self.audio_buffer = bytearray()

    def add_audio(self, audio: bytes):
        self.audio_buffer.extend(audio)

    def reset(self):
        self.audio_buffer.clear()

    async def recognize(self) -> str:
        # Ensure even number of bytes for int16
        trimmed = self.audio_buffer[:len(self.audio_buffer) - (len(self.audio_buffer) % 2)]
        samples = np.frombuffer(trimmed, dtype=np.int16).astype(np.float32) / 32768.0
        data = samples.tolist()

        async with websockets.connect(SHERPA_WS_URL) as ws:
            await ws.send(json.dumps({"samples": data}))
            response = await ws.recv()

        result = json.loads(response)
        return result.get("text", "")

class SherpaSTTServer(AsyncServer):
    async def handle(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        session = self.create_session(reader, writer)
        stt_session = SherpaSTTSession()

        async for message in session:
            if isinstance(message, StartListening):
                stt_session.reset()

            elif isinstance(message, Audio):
                stt_session.add_audio(message.audio)

            elif isinstance(message, StopListening):
                transcript = await stt_session.recognize()
                await session.write_message(Transcript(text=transcript))
                await session.write_message(StopListening())

async def main():
    server = SherpaSTTServer()
    await server.run()

if __name__ == "__main__":
    asyncio.run(main())
