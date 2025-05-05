#!/bin/bash
if [ ! -f /config/addons_config/k2fsa/downloaded ]; then
    mkdir -p /config/addons_config/k2fsa
    wget -O asr-model.tar.bz2 "https://ghfast.top/https://github.com/k2-fsa/sherpa-onnx/releases/download/asr-models/icefall-asr-zipformer-wenetspeech-20230615.tar.bz2" --no-check-certificate
    mkdir -p /k2fsa/module
    tar -xjf asr-model.tar.bz2 -C /config/addons_config/k2fsa --strip-components=3 icefall-asr-zipformer-wenetspeech-20230615/data/lang_char/tokens.txt
    tar -xjf asr-model.tar.bz2 -C /config/addons_config/k2fsa --strip-components=2 --wildcards '*/exp/*'
    rm -f asr-model.tar.bz2
    touch /config/addons_config/k2fsa/downloaded
else
    echo the model has been downloaded, skip downloading it again
fi
# 启动 Sherpa-ONNX WebSocket 服务器
/k2fsa/bin/sherpa-onnx-offline-websocket-server \
    --port=6006 \
    --num-work-threads=5 \
    --tokens=/config/addons_config/k2fsa/tokens.txt \
    --encoder=/config/addons_config/k2fsa/encoder-epoch-12-avg-4.onnx \
    --decoder=/config/addons_config/k2fsa/decoder-epoch-12-avg-4.onnx \
    --joiner=/config/addons_config/k2fsa/joiner-epoch-12-avg-4.onnx \
    --max-batch-size=5

# 启动 Wyoming 适配器
#python3 /k2fsa/wyoming_sherpa.py
