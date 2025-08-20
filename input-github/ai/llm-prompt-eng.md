<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-prompt-eng.md# -->

## プロンプトエンジニアリング | Prompt Engineering
- モデル出力の制御・最適化のために入力プロンプトを設計・工夫する技術全般。Zero-shot, Few-shot, CoTなどを含む。

## 文脈内学習 | In-Context Learning | ICL
- LLMの重みパラメータの更新をせずともプロンプト中に少数のデモ(あるタスクの入力例と望ましい回答のペア)を追加すると、LLMが一時的にそのタスクに適応する、そのタスクの回答精度が向上する現象。 ※ 上手くタスク適応/精度向上しないときもある。
- プロンプトに追加するデモの数に応じて、以下のように分類される。
  - Zero-Shot: いわゆる文脈無い学習適用前の状態。タスク説明のみでデモは含まない。
  - One-Shot: デモを1件を含む。
  - Few-Shot: デモを数件含む。

- 具体的: 英仏翻訳のタスクをIn-Context Learning(Few-Shot)するプロンプト
 - (引用元): Brown, Tom, et al. "Language models are few-shot learners." Advances in neural information processing systems 33 (2020): 1877-1901. https://arxiv.org/abs/2005.14165
```
Translate English to French:  ※ タスクの説明
sea otter => loutre de mer    ※ デモ1つ目
peppermint => menthe poivrée  ※ デモ2つ目
plush giraffe => girafe peluche ※ デモ3つ目
cheese =>  ※ タスク
```

## Chain-of-Thought | CoT
- モデルに推論過程（思考の連鎖）を明示的に生成させることで、複雑な問題に対する精度を高めるプロンプティング手法。
