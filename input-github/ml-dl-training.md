<!-- 記事タイトル:用語解説集-機械学習-深層学習-学習関連 -->
<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-training.md# -->

## 転移学習 | Transfer Learning <!-- entry_word_and_anchor:ML_DL_TRAIN_TransferLearning -->
- ファインチューニングと同様、ある学習済みAIモデルをもう一度学習させること。
- ただし、ファインチューニングとは違い、新たに学習させるタスクは学習済みAIモデルのタスクのサブセットと決まっているわけではない。似ているが同一でないタスクである。
- 一般的には、元の学習済みAIモデルに新たなレイヤーを追加しこの重みに新しいタスクを学習させる。既存のレイヤーはフリーズさせる。つまり、既存のレイヤーの学習率は0とする。

## ファインチューニング | Fine-tuning <!-- entry_word_and_anchor:ML_DL_TRAIN_FineTuning -->
- 転移学習と同様、ある学習済みAIモデルをもう一度学習させること。
- 一般的には、新たに学習させるタスクは学習済みAIモデルのタスクのサブセットである。
- 一般的には、元の学習済みAIモデルに新たなレイヤーを追加しこの重みに新しいタスクを学習させる。既存のレイヤーも学習させるが、既存のレイヤーの学習率は低めにする。
る。

## Zero-Shot Learning <!-- entry_word_and_anchor:ML_DL_TRAIN_ZeroShotLearning -->
- 教師データに無いカテゴリを予測する問題設定。

## Few-Shot Learning <!-- entry_word_and_anchor:ML_DL_TRAIN_FewShotLearning -->
- ファインチューニングや転移学習と同様、ある学習済みAIモデルをもう一度学習させること。
- ただし、ファインチューニングや転移学習は大量の教師データを用いるのが一般的であるが、非常に少量の教師データでAIモデルを学習させようとする問題設定。
