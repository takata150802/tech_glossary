<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md# -->

## 訓練データ | トレーニングデータ | Training Data <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_TrainingData -->
- モデルを学習させるために使用されるデータセットで、モデルがデータのパターンを認識し、予測や分類の能力を向上させるために利用されます。


## 過学習 | Overfitting <!-- entry_word_and_anchor:ML_DL_overfitting -->
- モデルが訓練データに過度に適合し、新しいデータに対して一般化できない状態を指します。
- 対策として、Dropoutが有名。

## 交差検証 | Cross-Validation <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_CrossValid -->
- データセットを複数の部分に分割してモデルを評価する手法であり、過学習を防ぎ、モデルの汎化性能を評価するのに役立ちます。


## 損失関数 | Loss Function <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_LossFunc -->
- モデルの予測と実際の値との間の誤差を計算する関数であり、モデルのパフォーマンスを評価し、最適化するために使用されます。


## word2vec | word2vec <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_word2vec-->
- 単語をベクトル形式で表現する技術であり、自然言語処理において単語間の意味的な類似性を捉えるために使用されます。

## ハイパーパラメータ | Hyperparameter <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Hyperparam -->
- モデルの学習過程で設定されるパラメータであり、学習率やバッチサイズなど、モデルの構造やトレーニングに影響を与えます。

## Batch Normalization <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_BatchNorm -->
- 各ミニバッチの平均と分散を標準化することで、学習を安定化させ、トレーニングの速度と性能を向上させる手法です。

## 確率的勾配降下法 | Stochastic Gradient Descent | SGD <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_SGD -->
- ランダムに選択されたデータポイントに基づいてモデルのパラメータを更新し、損失関数を最小化する最適化アルゴリズムです。

## ドロップアウト | Dropout <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Dropout -->
- トレーニング中にランダムに一部のノードを無効化することで、過学習を防ぎ、モデルの汎化性能を向上させる正則化手法です。

## 活性化関数 | Activation Function <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_ActivationFunc -->
- ニューラルネットワークの各ノードの出力に適用される関数であり、非線形性を導入して複雑なパターンを学習するのを助けます。

## Data Augmentation <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_DataAugmentation -->
- 既存のデータにランダムな変換（回転、ズーム、反転など）を加えることで、データセットを人工的に拡張し、モデルの汎化性能を向上させる手法です。

## バッチサイズ | Batch Size <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_BatchSize -->
- モデルのトレーニング中に一度に処理されるデータポイントの数を指し、トレーニングの速度と安定性に影響を与えます。

## エポック | Epoch <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Epoch -->
- トレーニングデータ全体をモデルが一度完全に通過することを指し、モデルがデータセットにどれだけ多くの回数適合されたかを示します。

## TensorFlow <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_TensorFlow -->
- Googleが開発したオープンソースのディープラーニングフレームワークであり、さまざまな機械学習モデルの構築とトレーニングに使用されます。

## PyTorch <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_PyTorch -->
- Facebookが開発したオープンソースのディープラーニングフレームワークであり、動的な計算グラフと直感的なAPIを提供し、研究と開発に広く利用されています。

## scikit-learn <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_scikitlearn -->
- Pythonの機械学習ライブラリであり、分類、回帰、クラスタリングなどの一般的な機械学習アルゴリズムを提供します。

## 勾配消失問題 | Vanishing Gradient Problem <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_VanishingGradientProblem -->
- 深いニューラルネットワークのトレーニング中に、勾配が小さくなりすぎて更新が効果的に行えなくなる問題。
- 対策として、ReLUやMaxOutなどの活性化関数の提案

## 誤差逆伝播法 | バックプロパゲーション | Backpropagation <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_BackProp -->
- ニューラルネットワークのトレーニングアルゴリズムであり、誤差を出力層から入力層に逆伝播させて、各層の重みを更新します。

## 学習率 | Learning Rate <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_LearningRate -->
- モデルのパラメータを更新する際のステップサイズを決定するハイパーパラメータであり、学習の収束速度と安定性に影響を与えます。

## Poolingレイヤー | Pooling Layer <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_PoolingLayer -->
- 畳み込みニューラルネットワークにおいて、特徴マップの空間次元を縮小し、計算量の削減と特徴の不変性を向上させる層です。

## 混同行列 | Confusion Matrix <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_ConfusionMatrix -->
- 分類モデルの性能を評価するための行列であり、真陽性、真陰性、偽陽性、偽陰性の数を示します。

## 次元の呪い | Curse of Dimensionality <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_CurseOfDim -->
- 高次元データにおいて、データのスパース性や距離計算の信頼性が低下し、機械学習アルゴリズムの性能が劣化する現象を指します。

## 説明可能なAI | Explainable AI | XAI <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_XAI -->
- モデルの予測や決定の背後にある理由を理解しやすくするための技術や手法の集合であり、透明性と信頼性を向上させます。

## ハルシネーション | Hallucination <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Hallucination -->
- 生成モデルが学習データに存在しない偽の情報を生成する現象を指します。

## F値 | F1 Score <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_F1Score -->
- 分類モデルの性能を評価する指標であり、適合率（Precision）と再現率（Recall）の調和平均を取ります。

## 偽陰性 | False Negative | FN <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_FalseNegative -->
- 実際にはポジティブであるが、モデルがネガティブと誤分類したデータポイントの数を指します。

## 偽陽性 | False Positive | FP <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_FalsePositive -->
- 実際にはネガティブであるが、モデルがポジティブと誤分類したデータポイントの数を指します。

## 適合率 | Precision <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Precision -->
- モデルがポジティブと予測したデータポイントのうち、実際にポジティブである割合を示す指標です。

## 再現率 | Recall <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Recall -->
- 実際にポジティブであるデータポイントのうち、モデルが正しくポジティブと予測した割合を示す指標です。

## MLOps <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_MLOps -->
- 機械学習モデルの開発、デプロイ、および運用を効率化するための手法とツールの集合であり、ソフトウェア開発のDevOpsに似た概念です。

## 訓練誤差 | Training Error <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_TrainingError -->
- モデルがトレーニングデータセットに対して予測した際の誤差を指し、モデルの学習が進むにつれて通常減少します。

## コサイン類似度 | Cosine Similarity <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_CosineSimilarity -->
- 二つのベクトルの間の類似度を計算する指標であり、ベクトルのなす角度のコサイン値を用います。

## スムージング | Smoothing <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Smoothing -->
- データのばらつきを減少させるために使用される手法であり、特に確率分布の推定や時系列データの予測において効果的です。

## KL情報量 | Kullback-Leibler Divergence | KL Divergence <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_KLDivergence -->
- 二つの確率分布間の差異を測定する指標であり、情報理論に基づいています。

## Early Stopping <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_EarlyStopping -->
- トレーニング中にモデルの性能が向上しなくなった時点で学習を停止する手法であり、過学習を防ぐのに役立ちます。

## ROC曲線 | ROC Curve <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_ROCCurve -->
- モデルの真陽性率と偽陽性率をプロットしたものであり、モデルの分類性能を評価するために使用されます。

## アノテーション | Annotation <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Annotation -->
- データセットに対してラベルやメタデータを付与する作業であり、特に教師あり学習において重要です。

## ロジット関数 | Logit Function <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_LogitFunc -->
- ロジスティック回帰モデルにおいて、確率をオッズ比に変換する関数です。

## Jaccard係数 | Jaccard Index <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_JaccardIndex -->
- 二つの集合の交差部分のサイズを和集合のサイズで割ったものであり、類似度を測定する指標です。

## t-SNE | t-Distributed Stochastic Neighbor Embedding | t-SNE <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_tSNE -->
- 高次元データを低次元空間に可視化するための次元削減手法です。

## オッズ比 | Odds Ratio <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Odds -->
- ある事象が起きる確率pに対し、p / ( 1 - p)で表される指標

## Logit <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Logit -->
- オッズ比の自然対数をとったもの 
- ある事象が起きる確立pに対しlog(p / (1 - p))で表せ、pを変数とするロジット関数とも呼ばれる
- ロジット関数の逆関数がシグモイド関数である。
