<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md# -->

## 事前学習 | Pretraining<a id="5LqL5YmN5a2m57+SIHwgUHJldHJhaW5pbmc="></a>

- 巨大な未ラベルデータセットを用いて、マスク言語モデルや<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#6Ieq5bex5Zue5biwIHwgQXV0b3JlZ3Jlc3NpdmU=">自己回帰</a>モデルの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5pCN5aSx6Zai5pWwIHwgTG9zcyBGdW5jdGlvbg==">損失関数</a>で学習を行う工程。

## LoRA | Low-Rank Adaptation<a id="TG9SQSB8IExvdy1SYW5rIEFkYXB0YXRpb24="></a>

- モデルの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg==">重み</a>の一部に低ランク行列を追加し、微調整時のパラメータ数を抑える<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#UEVGVCB8IFBhcmFtZXRlci1FZmZpY2llbnQgRmluZS1UdW5pbmc=">PEFT</a>手法の一種。

## PEFT | Parameter-Efficient Fine-Tuning<a id="UEVGVCB8IFBhcmFtZXRlci1FZmZpY2llbnQgRmluZS1UdW5pbmc="></a>

- 全パラメータではなく一部のみ更新することで、少数のリソースで<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmcgfCBGaW5lIHR1bmluZw==">ファインチューニング</a>を可能にする技術群。

## Instruction Tuning<a id="SW5zdHJ1Y3Rpb24gVHVuaW5n"></a>

- モデルにタスク指示文（instruction）を含むデータで<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmcgfCBGaW5lIHR1bmluZw==">ファインチューニング</a>し、指示に従った応答生成能力を向上させる手法。例：FLAN, <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-llm.md#VDUgfCBUZXh0LVRvLVRleHQgVHJhbnNmZXIgVHJhbnNmb3JtZXI=">T5</a>。

## RLHF | Reinforcement Learning from Human Feedback<a id="UkxIRiB8IFJlaW5mb3JjZW1lbnQgTGVhcm5pbmcgZnJvbSBIdW1hbiBGZWVkYmFjaw=="></a>

- 人間の好みを反映した報酬モデルを用いて、PPOなどの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5by35YyW5a2m57+SIHwgUmVpbmZvcmNlbWVudCBMZWFybmluZw==">強化学習</a>で<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>を微調整する手法。ChatGPTで活用。

## SFT | Supervised Fine-tuning<a id="U0ZUIHwgU3VwZXJ2aXNlZCBGaW5lLXR1bmluZw=="></a>

- 人間の生成例や指示に対する模範応答などを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5pWZ5bir44GC44KK5a2m57+SIHwgU3VwZXJ2aXNlZCBMZWFybmluZw==">教師あり学習</a>でモデルに学習させる工程。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#UkxIRiB8IFJlaW5mb3JjZW1lbnQgTGVhcm5pbmcgZnJvbSBIdW1hbiBGZWVkYmFjaw==">RLHF</a>の前段階として使われる。

## Self-Instruct<a id="U2VsZi1JbnN0cnVjdA=="></a>

- 既存の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>を用いて、自動的に命令データと模範応答を生成し、instruction tuning用のデータを自己生成する手法。

## Adapter Layers<a id="QWRhcHRlciBMYXllcnM="></a>

- モデルの特定の層に小さな追加モジュールを挿入し、微調整時に更新するパラメータを限定する技術。
- 用途: <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#UEVGVCB8IFBhcmFtZXRlci1FZmZpY2llbnQgRmluZS1UdW5pbmc=">PEFT</a>の一種として、効率的な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmcgfCBGaW5lIHR1bmluZw==">ファインチューニング</a>に使用。

## Prefix Tuning<a id="UHJlZml4IFR1bmluZw=="></a>

- モデルの入力に特定の「プレフィックス」を追加し、その部分のみを学習することでモデルを微調整する手法。

## Gradient Checkpointing<a id="R3JhZGllbnQgQ2hlY2twb2ludGluZw=="></a>

- 大規模な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の学習処理でのメモリ使用量を削減するために、中間勾配を再計算する技術。
