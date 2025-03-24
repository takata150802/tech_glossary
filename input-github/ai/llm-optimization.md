<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md# -->

## 蒸留 | Distillation
- 教師モデル（teacher）の出力を用いて、生徒モデル（student）を学習させる知識圧縮手法。

## 量子化 | Quantization
- FP32重みをINT8やBF16などの低ビット表現に変換し、モデルメモリフットプリントと推論速度を改善する。

## FP32 | Float32
- IEEE 754準拠の単精度浮動小数点表現。符号1ビット、指数8ビット、仮数23ビットで構成され、訓練時の安定性が高いが、メモリ帯域と計算量が大きい。

## FP16 | Float16
- 半精度浮動小数点表現。符号1ビット、指数5ビット、仮数10ビットを持ち、計算速度とメモリ効率を向上できるが、勾配消失や数値安定性に課題あり。Mixed Precision Trainingで利用される。

## BF16 | bfloat16
- Googleが提唱する16bit浮動小数点形式で、FP32と同じ8ビットの指数部を持ちつつ、仮数部を7ビットに圧縮。ダイナミックレンジを保ちつつ、演算効率を高める。TPUやNVIDIA Ampere以降で利用可。

## INT8 
- 整数8ビット表現。重みやアクティベーションを量子化することで、モデルのメモリ削減と推論高速化を実現。ポストトレーニン

