<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-prompt-eng.md# -->

## プロンプトエンジニアリング | Prompt Engineering<a id="44OX44Ot44Oz44OX44OI44Ko44Oz44K444OL44Ki44Oq44Oz44KwIHwgUHJvbXB0IEVuZ2luZWVyaW5n"></a>

- モデル出力の制御・最適化のために入力<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OX44Ot44Oz44OX44OIIHwgUHJvbXB0">プロンプト</a>を設計・工夫する技術全般。Zero-shot, Few-shot, <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-prompt-eng.md#Q2hhaW4tb2YtVGhvdWdodCB8IENvVA==">CoT</a>などを含む。

## 文脈内学習 | In-Context Learning | ICL<a id="5paH6ISI5YaF5a2m57+SIHwgSW4tQ29udGV4dCBMZWFybmluZyB8IElDTA=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg==">重みパラメータ</a>の更新をせずとも<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OX44Ot44Oz44OX44OIIHwgUHJvbXB0">プロンプト</a>中に少数のデモ(あるタスクの入力例と望ましい回答のペア)を追加すると、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>が一時的にそのタスクに適応する、そのタスクの回答精度が向上する現象。 ※ 上手くタスク適応/精度向上しないときもある。

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OX44Ot44Oz44OX44OIIHwgUHJvbXB0">プロンプト</a>に追加するデモの数に応じて、以下のように<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>される。

  - Zero-Shot: いわゆる文脈無い学習適用前の状態。タスク説明のみでデモは含まない。
  - One-Shot: デモを1件を含む。
  - Few-Shot: デモを数件含む。

- 具体的: 英仏翻訳のタスクを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-prompt-eng.md#5paH6ISI5YaF5a2m57+SIHwgSW4tQ29udGV4dCBMZWFybmluZyB8IElDTA==">In-Context Learning</a>(Few-Shot)する<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OX44Ot44Oz44OX44OIIHwgUHJvbXB0">プロンプト</a>

- (引用元): Brown, Tom, et al. "Language models are few-shot learners." Advances in neural information processing systems 33 (2020): 1877-1901. https://arxiv.org/abs/2005.14165

```
Translate English to French:  ※ タスクの説明
sea otter => loutre de mer    ※ デモ1つ目
peppermint => menthe poivrée  ※ デモ2つ目
plush giraffe => girafe peluche ※ デモ3つ目
cheese =>  ※ タスク
```

## Chain-of-Thought | CoT<a id="Q2hhaW4tb2YtVGhvdWdodCB8IENvVA=="></a>

- モデルに<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>過程（思考の連鎖）を明示的に生成させることで、複雑な問題に対する精度を高めるプロンプティング手法。
