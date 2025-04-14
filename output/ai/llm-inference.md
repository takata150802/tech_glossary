<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md# -->

## LLM推論サーバー | LLM Inference Server<a id="TExN5o6o6KuW44K144O844OQ44O8IHwgTExNIEluZmVyZW5jZSBTZXJ2ZXI="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>を効率的に実行するためのソフトウェア
- 具体例:
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md#dkxMTQ==">vLLM</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md#TlZJRElBIFRyaXRvbiBJbmZlcmVuY2UgU2VydmVy">NVIDIA Triton Inference Server</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md#SHVnZ2luZyBGYWNlIFRHSSB8IFRHSQ==">Hugging Face TGI</a>

## vLLM<a id="dkxMTQ=="></a>

- GitHub https://github.com/vllm-project/vllm
- ライセンス: Apache License 2.0 ​
- UC BerkeleyのSky Computing Labが開発
- 高スループットかつメモリ効率の良い<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md#TExN5o6o6KuW44K144O844OQ44O8IHwgTExNIEluZmVyZW5jZSBTZXJ2ZXI=">LLM推論サーバー</a>。
  - Paged<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwgQXR0ZW50aW9u">Attention</a>
  - In-flight batching
  - Speculative Decoding
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#Rmxhc2hBdHRlbnRpb24=">FlashAttention</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/llm-overview.md#T3BlbkFJ">OpenAI</a>互換API
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#TG9SQSB8IExvdy1SYW5rIEFkYXB0YXRpb24=">LoRA</a>対応
    \- マルチGPU・マルチノード分散<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>

## Hugging Face TGI | TGI<a id="SHVnZ2luZyBGYWNlIFRHSSB8IFRHSQ=="></a>

- GitHub: https://github.com/huggingface/text-generation-inference
- ライセンス: Apache License 2.0
  - ひと悶着: HFOIL 1.0なるライセンスに変更しようとして頓挫 https://github.com/huggingface/text-generation-inference/issues/726
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/llm-overview.md#SHVnZ2luZyBGYWNl">Hugging Face</a>が開発したRust/Python製の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md#TExN5o6o6KuW44K144O844OQ44O8IHwgTExNIEluZmVyZW5jZSBTZXJ2ZXI=">LLM推論サーバー</a>。
  - Llama、Falcon、GPT-NeoXなどのモデルに対応
  - Tensor Parallelism
  - SSEによる<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>ストリーミング
  - Continuous batching
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#Rmxhc2hBdHRlbnRpb24=">FlashAttention</a>
  - Paged<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwgQXR0ZW50aW9u">Attention</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md#6YeP5a2Q5YyWIHwgUXVhbnRpemF0aW9u">量子化</a>（bitsandbytes、GPTQ、AWQなど）
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/llm-overview.md#T3BlbkFJ">OpenAI</a> Chat API互換のMessages API

## NVIDIA Triton Inference Server<a id="TlZJRElBIFRyaXRvbiBJbmZlcmVuY2UgU2VydmVy"></a>

- GitHub: https://github.com/triton-inference-server/server
- ライセンス: BSD 3-Clause License​
- NVIDIAが提供する高性能な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md#TExN5o6o6KuW44K144O844OQ44O8IHwgTExNIEluZmVyZW5jZSBTZXJ2ZXI=">LLM推論サーバー</a>。
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md#VGVuc29yUlQtTExN">TensorRT-LLM</a>、ONNX Runtime、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md#dkxMTQ==">vLLM</a>など複数のバックエンドを統合
  - マルチモデル・マルチフレームワークの同時<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>
  - バッチ処理
  - モデルのバージョン管理
  - Prometheusによるモニタリング
  - Kubernetesとの統合

## TensorRT-LLM<a id="VGVuc29yUlQtTExN"></a>

- GitHub: https://github.com/NVIDIA/<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md#VGVuc29yUlQtTExN">TensorRT-LLM</a>
- ライセンス: Apache-2.0 license
- NVIDIAが提供するTensorRTの上に構築された<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a><a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>エンジン。
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5YG96Zm95oCnIHwgRmFsc2UgUG9zaXRpdmUgfCBGUA==">FP</a>8、INT4、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md#SU5UOA==">INT8</a>などの低精度<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>
  - In-flight batching
  - Speculative Decoding（Medusa、EAGLE、ReDrafter）
  - Paged KV Cache
  - TensorRTと統合して高性能な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>を実現

## llama.cpp<a id="bGxhbWEuY3Bw"></a>

- GitHub: https://github.com/ggerganov/<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md#bGxhbWEuY3Bw">llama.cpp</a>
- ライセンス: MIT License
- C++で実装された軽量な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a><a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>エンジン。
  - CPU上での高速<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>
    - マルチスレッド<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md#6YeP5a2Q5YyWIHwgUXVhbnRpemF0aW9u">量子化</a>（INT4、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md#SU5UOA==">INT8</a>）
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#TG9SQSB8IExvdy1SYW5rIEFkYXB0YXRpb24=">LoRA</a>

## Ollama<a id="T2xsYW1h"></a>

- GitHub: https://github.com/jmorganca/ollama
- ライセンス: MIT License​
- ローカル環境での<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a><a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>を簡単に行うためのツール。
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/llm-overview.md#T3BlbkFJ">OpenAI</a> API互換のインターフェース
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md#bGxhbWEuY3Bw">llama.cpp</a>を内部で利用し、モデルの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>を実行
  - モデルの自動ダウンロードと管理
  - DockerベースでLlama 2、Mistral、Code Llamaなどのモデルをサポート
  - GPU/CPU対応
