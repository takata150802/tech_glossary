<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md# -->

## 事前学習 | Pre-training<a id="5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>のモデル開発を大きく3つのステップに分けたときの最初のステップ。
  - **ステップ1. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n">事前学習</a> ★**
  - ステップ2. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5oyH56S65a2m57+SIHwgSW5zdHJ1Y3Rpb24gdHVuaW5n">指示学習</a>
  - ステップ3. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#44Ki44Op44Kk44Oz44Oh44Oz44OIIHwgQWxpZ25tZW50">アラインメント</a>
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5pWZ5bir44Gq44GX5a2m57+SIHwgVW5zdXBlcnZpc2VkIExlYXJuaW5n">教師なし学習</a>。データセットは、Web上から収集した膨大なテキストデータを学習し知識を獲得するステップ。
- 具体的には、以下二つのような予測タスクを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>に学習させる。人手でラベル付けする(=望ましい<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の出力を作成する)必要がない。したがって、膨大なテキストデータを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>に学習させることを実現し、大きなブレイクスルーとなった。
  - Next-token prediction: 次の単語の予測
  - Masked language modeling: ランダムにマスクされた単語の予測
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n">事前学習</a>したモデルは、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5Z+655uk44Oi44OH44OrIHwgRm91bmRhdGlvbiBNb2RlbA==">基盤モデル</a>と呼ばれる。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n">事前学習</a>を実施するのにあたり、計算資源、データセット、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>のパラメータ数の規模をどの程度にするか？が重要であり、その指標としてScaling lawsがある。
- 数千枚以上のGPUを使用する分散学習を行う。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n">事前学習</a>をどのように数千枚のGPUに分散するか？は重要な研究開発領域となっている。

## 指示学習 | Instruction tuning<a id="5oyH56S65a2m57+SIHwgSW5zdHJ1Y3Rpb24gdHVuaW5n"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>のモデル開発を大きく3つのステップに分けたときの2番目のステップ。
  - ステップ1. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n">事前学習</a>
  - **ステップ2. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5oyH56S65a2m57+SIHwgSW5zdHJ1Y3Rpb24gdHVuaW5n">指示学習</a> ★**
  - ステップ3. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#44Ki44Op44Kk44Oz44Oh44Oz44OIIHwgQWxpZ25tZW50">アラインメント</a>
- 一般的に、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5pWZ5bir44GC44KK5a2m57+SIHwgU3VwZXJ2aXNlZCBMZWFybmluZw==">教師あり学習</a>の一種である<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#U0ZUIHwgU3VwZXJ2aXNlZCBGaW5lLXR1bmluZw==">SFT</a>と呼ばれる手法を用いて、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5Z+655uk44Oi44OH44OrIHwgRm91bmRhdGlvbiBNb2RlbA==">基盤モデル</a>をQ&A、翻訳、要約、センチメント分析、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>などのタスク向けに<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc=">Fine-tuning</a>するステップ。
- 下記の論文が初めて"<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5oyH56S65a2m57+SIHwgSW5zdHJ1Y3Rpb24gdHVuaW5n">Instruction tuning</a>"という用語を提唱した。
  - <a href="https://arxiv.org/abs/2109.01652"> Wei, Jason, et al. "Finetuned language models are zero-shot learners." arXiv preprint arXiv:2109.01652 (2021). </a>
  - 従来は、各タスク毎に別々にモデルを開発していた。あるいは、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-llm.md#QkVSVCB8IEJpZGlyZWN0aW9uYWwgRW5jb2RlciBSZXByZXNlbnRhdGlvbnMgZnJvbSBUcmFuc2Zvcm1lcnM=">BERT</a>などのある共通のモデルを各タスク向けに<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc=">Fine-tuning</a>するにしてもどのタスクか?を示す特殊な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を導入するなどして形式が統一的でなかった。
  - 本論文以降、ある1つの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5Z+655uk44Oi44OH44OrIHwgRm91bmRhdGlvbiBNb2RlbA==">基盤モデル</a>に対し、様々なタスクの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>への指示文と望ましい応答のペアという形式が統一的なデータセットを使って<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc=">Fine-tuning</a>することが一般的となった。

## アラインメント | Alignment<a id="44Ki44Op44Kk44Oz44Oh44Oz44OIIHwgQWxpZ25tZW50"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>のモデル開発を大きく3つのステップに分けたときの最後のステップ。
  - ステップ1. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n">事前学習</a>
  - ステップ2. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5oyH56S65a2m57+SIHwgSW5zdHJ1Y3Rpb24gdHVuaW5n">指示学習</a>
  - **ステップ3. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#44Ki44Op44Kk44Oz44Oh44Oz44OIIHwgQWxpZ25tZW50">アラインメント</a> ★**
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5oyH56S65a2m57+SIHwgSW5zdHJ1Y3Rpb24gdHVuaW5n">指示学習</a>した<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>を人間の価値基準・倫理・安全性要件に沿って調整させるステップ。
- 一般的に、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6Ieq5bex5pWZ5bir44GC44KK5a2m57+SIHwgU2VsZi1zdXBlcnZpc2VkIExlYXJuaW5n">自己教師あり学習</a>の一種である<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#UkxIRiB8IFJlaW5mb3JjZW1lbnQgTGVhcm5pbmcgZnJvbSBIdW1hbiBGZWVkYmFjaw==">RLHF</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5pWZ5bir44GC44KK5a2m57+SIHwgU3VwZXJ2aXNlZCBMZWFybmluZw==">教師あり学習</a>の一種であるDPOなどの手法が用いられる。
- Open<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>社のChatGPTがこの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#44Ki44Op44Kk44Oz44Oh44Oz44OIIHwgQWxpZ25tZW50">アラインメント</a>をRLFHという<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5by35YyW5a2m57+SIHwgUmVpbmZvcmNlbWVudCBMZWFybmluZw==">強化学習</a>ベースの手法で実施しているということで注目を集めたが、技術的詳細はクローズドで実際のところこの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#UkxIRiB8IFJlaW5mb3JjZW1lbnQgTGVhcm5pbmcgZnJvbSBIdW1hbiBGZWVkYmFjaw==">RLHF</a>がどのくらい有効なのかはよくわかっていない。

## 事後学習 | Post-training<a id="5LqL5b6M5a2m57+SIHwgUG9zdC10cmFpbmluZw=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>のモデル開発を大きく3つのステップに分けたとき、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n">事前学習</a>(1番目のステップ)の後に実施するステップという意味で、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5oyH56S65a2m57+SIHwgSW5zdHJ1Y3Rpb24gdHVuaW5n">指示学習</a>と<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#44Ki44Op44Kk44Oz44Oh44Oz44OIIHwgQWxpZ25tZW50">アラインメント</a>の総称として使われることがある。
  - ステップ1. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n">事前学習</a>
  - **ステップ2. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5oyH56S65a2m57+SIHwgSW5zdHJ1Y3Rpb24gdHVuaW5n">指示学習</a> ★**
  - **ステップ3. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#44Ki44Op44Kk44Oz44Oh44Oz44OIIHwgQWxpZ25tZW50">アラインメント</a> ★**

## 基盤モデル | Foundation Model<a id="5Z+655uk44Oi44OH44OrIHwgRm91bmRhdGlvbiBNb2RlbA=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n">事前学習</a>で膨大なテキストデータを学習した<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>のこと。
- 様々なタスク(Q&A、翻訳、要約、センチメント分析、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>)向けに<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5oyH56S65a2m57+SIHwgSW5zdHJ1Y3Rpb24gdHVuaW5n">指示学習</a>できる。

## SFT | Supervised Fine-tuning<a id="U0ZUIHwgU3VwZXJ2aXNlZCBGaW5lLXR1bmluZw=="></a>

- 特に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の学習に関して使われる用語で、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5Z+655uk44Oi44OH44OrIHwgRm91bmRhdGlvbiBNb2RlbA==">基盤モデル</a>に対して、あるタスクのデータセット(<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>への指示文と望ましい応答のペア)を用意し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc=">Fine-tuning</a>する。
- タスクとは具体的には、Q&A、翻訳、要約、センチメント分析、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>など。

## LoRA | Low-Rank Adaptation<a id="TG9SQSB8IExvdy1SYW5rIEFkYXB0YXRpb24="></a>

- モデルの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg==">重み</a>の一部に低ランク行列を追加し、微調整時のパラメータ数を抑える<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#UEVGVCB8IFBhcmFtZXRlci1FZmZpY2llbnQgRmluZS1UdW5pbmc=">PEFT</a>手法の一種。

## PEFT | Parameter-Efficient Fine-Tuning<a id="UEVGVCB8IFBhcmFtZXRlci1FZmZpY2llbnQgRmluZS1UdW5pbmc="></a>

- 全パラメータではなく一部のみ更新することで、少数のリソースで<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc=">ファインチューニング</a>を可能にする技術群。

## Instruction Tuning<a id="SW5zdHJ1Y3Rpb24gVHVuaW5n"></a>

- モデルにタスク指示文（instruction）を含むデータで<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc=">ファインチューニング</a>し、指示に従った応答生成能力を向上させる手法。例：FLAN, <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-llm.md#VDUgfCBUZXh0LVRvLVRleHQgVHJhbnNmZXIgVHJhbnNmb3JtZXI=">T5</a>。

## RLHF | Reinforcement Learning from Human Feedback<a id="UkxIRiB8IFJlaW5mb3JjZW1lbnQgTGVhcm5pbmcgZnJvbSBIdW1hbiBGZWVkYmFjaw=="></a>

- 人間の好みを反映した報酬モデルを用いて、PPOなどの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5by35YyW5a2m57+SIHwgUmVpbmZvcmNlbWVudCBMZWFybmluZw==">強化学習</a>で<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>を微調整する手法。ChatGPTで活用。

## Self-Instruct<a id="U2VsZi1JbnN0cnVjdA=="></a>

- 既存の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>を用いて、自動的に命令データと模範応答を生成し、instruction tuning用のデータを自己生成する手法。

## Adapter Layers<a id="QWRhcHRlciBMYXllcnM="></a>

- モデルの特定の層に小さな追加モジュールを挿入し、微調整時に更新するパラメータを限定する技術。
- 用途: <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#UEVGVCB8IFBhcmFtZXRlci1FZmZpY2llbnQgRmluZS1UdW5pbmc=">PEFT</a>の一種として、効率的な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc=">ファインチューニング</a>に使用。

## Prefix Tuning<a id="UHJlZml4IFR1bmluZw=="></a>

- モデルの入力に特定の「プレフィックス」を追加し、その部分のみを学習することでモデルを微調整する手法。

## Gradient Checkpointing<a id="R3JhZGllbnQgQ2hlY2twb2ludGluZw=="></a>

- 大規模な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の学習処理でのメモリ使用量を削減するために、中間勾配を再計算する技術。
