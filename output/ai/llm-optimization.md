<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md# -->

## 蒸留 | Distillation<a id="6JK455WZIHwgRGlzdGlsbGF0aW9u"></a>

- 教師モデル（teacher）の出力を用いて、生徒モデル（student）を学習させる知識圧縮手法。

## 量子化 | Quantization<a id="6YeP5a2Q5YyWIHwgUXVhbnRpemF0aW9u"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md#RlAzMiB8IEZsb2F0MzI=">FP32</a><a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg==">重み</a>を<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md#SU5UOA==">INT8</a>や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md#QkYxNiB8IGJmbG9hdDE2">BF16</a>などの低ビット表現に変換し、モデルメモリフットプリントと<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>速度を改善する。

## FP32 | Float32<a id="RlAzMiB8IEZsb2F0MzI="></a>

- IEEE 754準拠の単精度浮動小数点表現。符号1ビット、指数8ビット、仮数23ビットで構成され、訓練時の安定性が高いが、メモリ帯域と計算量が大きい。

## FP16 | Float16<a id="RlAxNiB8IEZsb2F0MTY="></a>

- 半精度浮動小数点表現。符号1ビット、指数5ビット、仮数10ビットを持ち、計算速度とメモリ効率を向上できるが、勾配消失や数値安定性に課題あり。Mixed <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#6YGp5ZCI546HIHwgUHJlY2lzaW9u">Precision</a> Trainingで利用される。

## BF16 | bfloat16<a id="QkYxNiB8IGJmbG9hdDE2"></a>

- Googleが提唱する16bit浮動小数点形式で、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md#RlAzMiB8IEZsb2F0MzI=">FP32</a>と同じ8ビットの指数部を持ちつつ、仮数部を7ビットに圧縮。ダイナミックレンジを保ちつつ、演算効率を高める。TPUやNVIDIA Ampere以降で利用可。

## INT8<a id="SU5UOA=="></a>

- 整数8ビット表現。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg==">重み</a>やアクティベーションを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md#6YeP5a2Q5YyWIHwgUXVhbnRpemF0aW9u">量子化</a>することで、モデルのメモリ削減と<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>高速化を実現。ポストトレーニン
