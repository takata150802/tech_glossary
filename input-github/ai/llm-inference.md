<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-inference.md.md# -->


## LLM推論サーバー | LLM Inference Server

- LLMの推論を効率的に実行するためのソフトウェア
- 具体例:
  - vLLM
  - NVIDIA Triton Inference Server
  - Hugging Face TGI

## vLLM

- GitHub https://github.com/vllm-project/vllm
- ライセンス: Apache License 2.0 ​
- UC BerkeleyのSky Computing Labが開発
- 高スループットかつメモリ効率の良いLLM推論サーバー。
  - PagedAttention
  - In-flight batching
  - Speculative Decoding
  - FlashAttention
  - OpenAI互換API
  - LoRA対応
　 - マルチGPU・マルチノード分散推論

## Hugging Face TGI | TGI

- GitHub: https://github.com/huggingface/text-generation-inference
- ライセンス: Apache License 2.0
    - ひと悶着: HFOIL 1.0なるライセンスに変更しようとして頓挫 https://github.com/huggingface/text-generation-inference/issues/726 
- Hugging Faceが開発したRust/Python製のLLM推論サーバー。
    - Llama、Falcon、GPT-NeoXなどのモデルに対応
    - Tensor Parallelism
    - SSEによるトークンストリーミング
    - Continuous batching
    - FlashAttention
    - PagedAttention
    - 量子化（bitsandbytes、GPTQ、AWQなど）
    - OpenAI Chat API互換のMessages API

## NVIDIA Triton Inference Server

- GitHub: https://github.com/triton-inference-server/server
- ライセンス: BSD 3-Clause License​
- NVIDIAが提供する高性能なLLM推論サーバー。
    - TensorRT-LLM、ONNX Runtime、vLLMなど複数のバックエンドを統合
    - マルチモデル・マルチフレームワークの同時推論
    - バッチ処理
    - モデルのバージョン管理
    - Prometheusによるモニタリング
    - Kubernetesとの統合

## TensorRT-LLM

- GitHub: https://github.com/NVIDIA/TensorRT-LLM
- ライセンス: Apache-2.0 license
- NVIDIAが提供するTensorRTの上に構築されたLLM推論エンジン。
    - FP8、INT4、INT8などの低精度推論
    - In-flight batching
    - Speculative Decoding（Medusa、EAGLE、ReDrafter）
    - Paged KV Cache
    - TensorRTと統合して高性能な推論を実現

## llama.cpp

- GitHub: https://github.com/ggerganov/llama.cpp
- ライセンス: MIT License
-  C++で実装された軽量なLLM推論エンジン。
    - CPU上での高速推論
        - マルチスレッド推論
    - 量子化（INT4、INT8）
    - LoRA

## Ollama

- GitHub: https://github.com/jmorganca/ollama
- ライセンス: MIT License​
- ローカル環境でのLLM推論を簡単に行うためのツール。
    - OpenAI API互換のインターフェース
    - llama.cppを内部で利用し、モデルの推論を実行
    - モデルの自動ダウンロードと管理
    - DockerベースでLlama 2、Mistral、Code Llamaなどのモデルをサポート
    - GPU/CPU対応

## KVキャッシュ | KV Cache
- 推論中に過去のキーとバリュー（Key/Value）を保存しておき、次のトークン予測時に再利用することで、再計算を避けて推論速度を大幅に向上させる技術。

## Speculative Decoding | 投機的デコーディング
- 小さく高速な言語モデルで仮予測を生成し、それを大きなモデルで検証・補完することで推論を高速化する仕組み。OpenAIのMedusaやMetaのEAGLEなどが代表例。

## In-Flight Batching
- 同時到着でなく逐次到着するユーザーリクエストを即座にバッチ化し、高スループットな推論を実現する仕組み。LLM推論サーバーの効率化に重要。