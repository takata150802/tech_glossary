<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md# -->

## 事前学習 | Pretraining
- 巨大な未ラベルデータセットを用いて、マスク言語モデルや自己回帰モデルの損失関数で学習を行う工程。

## LoRA | Low-Rank Adaptation
- モデルの重みの一部に低ランク行列を追加し、微調整時のパラメータ数を抑えるPEFT手法の一種。

## PEFT | Parameter-Efficient Fine-Tuning
- 全パラメータではなく一部のみ更新することで、少数のリソースでファインチューニングを可能にする技術群。

## Instruction Tuning
- モデルにタスク指示文（instruction）を含むデータでファインチューニングし、指示に従った応答生成能力を向上させる手法。例：FLAN, T5。

## RLHF | Reinforcement Learning from Human Feedback
- 人間の好みを反映した報酬モデルを用いて、PPOなどの強化学習でLLMを微調整する手法。ChatGPTで活用。

## SFT | Supervised Fine-tuning
- 人間の生成例や指示に対する模範応答などを教師あり学習でモデルに学習させる工程。RLHFの前段階として使われる。

## Self-Instruct
- 既存のLLMを用いて、自動的に命令データと模範応答を生成し、instruction tuning用のデータを自己生成する手法。

## Adapter Layers
- モデルの特定の層に小さな追加モジュールを挿入し、微調整時に更新するパラメータを限定する技術。
- 用途: PEFTの一種として、効率的なファインチューニングに使用。

## Prefix Tuning
- モデルの入力に特定の「プレフィックス」を追加し、その部分のみを学習することでモデルを微調整する手法。

## Gradient Checkpointing
- 大規模なLLMの学習処理でのメモリ使用量を削減するために、中間勾配を再計算する技術。
