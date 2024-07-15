<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md# -->

<a id="ML_DL_TRAIN_EVAL_TrainingData"></a>
## 訓練データ | トレーニングデータ | Training Data <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_TrainingData -->
- モデルを学習させるために使用されるデータセットで、モデルがデータのパターンを認識し、予測や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Classification"> 分類 </a>の能力を向上させるために利用されます。


<a id="ML_DL_overfitting"></a>
## 過学習 | Overfitting <!-- entry_word_and_anchor:ML_DL_overfitting -->
- モデルが<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_TrainingData"> 訓練データ </a>に過度に適合し、新しいデータに対して一般化できない状態を指します。
- 対策として、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_Dropout"> Dropout </a>が有名。

<a id="ML_DL_TRAIN_EVAL_CrossValid"></a>
## 交差検証 | Cross-Validation <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_CrossValid -->
- データセットを複数の部分に分割してモデルを評価する手法であり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_overfitting"> 過学習 </a>を防ぎ、モデルの汎化性能を評価するのに役立ちます。


<a id="ML_DL_TRAIN_EVAL_LossFunc"></a>
## 損失関数 | Loss Function <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_LossFunc -->
- モデルの予測と実際の値との間の誤差を計算する関数であり、モデルのパフォーマンスを評価し、最適化するために使用されます。


## word2vec | word2vec <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_word2vec-->
- 単語をベクトル形式で表現する技術であり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_NLP"> 自然言語処理 </a>において単語間の意味的な類似性を捉えるために使用されます。

<a id="ML_DL_TRAIN_EVAL_Hyperparam"></a>
## ハイパーパラメータ | Hyperparameter <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Hyperparam -->
- モデルの学習過程で設定されるパラメータであり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_LearningRate"> 学習率 </a>や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_BatchSize"> バッチサイズ </a>など、モデルの構造やトレーニングに影響を与えます。

<a id="ML_DL_TRAIN_EVAL_BatchNorm"></a>
## Batch Normalization <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_BatchNorm -->
- 各ミニバッチの平均と分散を<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Standardization"> 標準化 </a>することで、学習を安定化させ、トレーニングの速度と性能を向上させる手法です。

<a id="ML_DL_TRAIN_EVAL_SGD"></a>
## 確率的勾配降下法 | Stochastic Gradient Descent | SGD <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_SGD -->
- ランダムに選択されたデータポイントに基づいてモデルのパラメータを更新し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_LossFunc"> 損失関数 </a>を最小化する最適化アルゴリズムです。

<a id="ML_DL_TRAIN_EVAL_Dropout"></a>
## ドロップアウト | Dropout <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Dropout -->
- トレーニング中にランダムに一部のノードを無効化することで、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_overfitting"> 過学習 </a>を防ぎ、モデルの汎化性能を向上させる正則化手法です。

<a id="ML_DL_TRAIN_EVAL_ActivationFunc"></a>
## 活性化関数 | Activation Function <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_ActivationFunc -->
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_Neural_Network"> ニューラルネットワーク </a>の各ノードの出力に適用される関数であり、非線形性を導入して複雑なパターンを学習するのを助けます。

<a id="ML_DL_TRAIN_EVAL_DataAugmentation"></a>
## Data Augmentation <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_DataAugmentation -->
- 既存のデータにランダムな変換（回転、ズーム、反転など）を加えることで、データセットを人工的に拡張し、モデルの汎化性能を向上させる手法です。

<a id="ML_DL_TRAIN_EVAL_BatchSize"></a>
## バッチサイズ | Batch Size <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_BatchSize -->
- モデルのトレーニング中に一度に処理されるデータポイントの数を指し、トレーニングの速度と安定性に影響を与えます。

<a id="ML_DL_TRAIN_EVAL_Epoch"></a>
## エポック | Epoch <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Epoch -->
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_TrainingData"> トレーニングデータ </a>全体をモデルが一度完全に通過することを指し、モデルがデータセットにどれだけ多くの回数適合されたかを示します。

<a id="ML_DL_TRAIN_EVAL_TensorFlow"></a>
## TensorFlow <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_TensorFlow -->
- Googleが開発したオープンソースのディープラーニングフレームワークであり、さまざまな<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_ML"> 機械学習 </a>モデルの構築とトレーニングに使用されます。

<a id="ML_DL_TRAIN_EVAL_PyTorch"></a>
## PyTorch <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_PyTorch -->
- Facebookが開発したオープンソースのディープラーニングフレームワークであり、動的な計算グラフと直感的なAPIを提供し、研究と開発に広く利用されています。

<a id="ML_DL_TRAIN_EVAL_scikitlearn"></a>
## scikit-learn <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_scikitlearn -->
- Pythonの機械学習ライブラリであり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Classification"> 分類 </a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Regression"> 回帰 </a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Clustering"> クラスタリング </a>などの一般的な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_ML"> 機械学習 </a>アルゴリズムを提供します。

<a id="ML_DL_TRAIN_EVAL_VanishingGradientProblem"></a>
## 勾配消失問題 | Vanishing Gradient Problem <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_VanishingGradientProblem -->
- 深い<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_Neural_Network"> ニューラルネットワーク </a>のトレーニング中に、勾配が小さくなりすぎて更新が効果的に行えなくなる問題。
- 対策として、ReLUやMaxOutなどの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_ActivationFunc"> 活性化関数 </a>の提案

<a id="ML_DL_TRAIN_EVAL_BackProp"></a>
## 誤差逆伝播法 | バックプロパゲーション | Backpropagation <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_BackProp -->
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_Neural_Network"> ニューラルネットワーク </a>のトレーニングアルゴリズムであり、誤差を出力層から入力層に逆伝播させて、各層の重みを更新します。

<a id="ML_DL_TRAIN_EVAL_LearningRate"></a>
## 学習率 | Learning Rate <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_LearningRate -->
- モデルのパラメータを更新する際のステップサイズを決定する<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_Hyperparam"> ハイパーパラメータ </a>であり、学習の収束速度と安定性に影響を与えます。

<a id="ML_DL_TRAIN_EVAL_PoolingLayer"></a>
## Poolingレイヤー | Pooling Layer <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_PoolingLayer -->
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_CNN"> 畳み込みニューラルネットワーク </a>において、特徴マップの空間次元を縮小し、計算量の削減と特徴の不変性を向上させる層です。

<a id="ML_DL_TRAIN_EVAL_ConfusionMatrix"></a>
## 混同行列 | Confusion Matrix <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_ConfusionMatrix -->
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Classification"> 分類 </a>モデルの性能を評価するための行列であり、真陽性、真陰性、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_FalsePositive"> 偽陽性 </a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_FalseNegative"> 偽陰性 </a>の数を示します。

<a id="ML_DL_TRAIN_EVAL_CurseOfDim"></a>
## 次元の呪い | Curse of Dimensionality <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_CurseOfDim -->
- 高次元データにおいて、データのスパース性や距離計算の信頼性が低下し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_ML"> 機械学習 </a>アルゴリズムの性能が劣化する現象を指します。

<a id="ML_DL_TRAIN_EVAL_XAI"></a>
## 説明可能なAI | Explainable AI | XAI <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_XAI -->
- モデルの予測や決定の背後にある理由を理解しやすくするための技術や手法の集合であり、透明性と信頼性を向上させます。

<a id="ML_DL_TRAIN_EVAL_Hallucination"></a>
## ハルシネーション | Hallucination <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Hallucination -->
- 生成モデルが学習データに存在しない偽の情報を生成する現象を指します。

<a id="ML_DL_TRAIN_EVAL_F1Score"></a>
## F値 | F1 Score <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_F1Score -->
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Classification"> 分類 </a>モデルの性能を評価する指標であり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_Precision"> 適合率 </a>（<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_Precision"> Precision </a>）と<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_Recall"> 再現率 </a>（<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_Recall"> Recall </a>）の調和平均を取ります。

<a id="ML_DL_TRAIN_EVAL_FalseNegative"></a>
## 偽陰性 | False Negative | FN <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_FalseNegative -->
- 実際にはポジティブであるが、モデルがネガティブと誤<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Classification"> 分類 </a>したデータポイントの数を指します。

<a id="ML_DL_TRAIN_EVAL_FalsePositive"></a>
## 偽陽性 | False Positive | FP <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_FalsePositive -->
- 実際にはネガティブであるが、モデルがポジティブと誤<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Classification"> 分類 </a>したデータポイントの数を指します。

<a id="ML_DL_TRAIN_EVAL_Precision"></a>
## 適合率 | Precision <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Precision -->
- モデルがポジティブと予測したデータポイントのうち、実際にポジティブである割合を示す指標です。

<a id="ML_DL_TRAIN_EVAL_Recall"></a>
## 再現率 | Recall <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Recall -->
- 実際にポジティブであるデータポイントのうち、モデルが正しくポジティブと予測した割合を示す指標です。

<a id="ML_DL_TRAIN_EVAL_MLOps"></a>
## MLOps <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_MLOps -->
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_ML"> 機械学習 </a>モデルの開発、デプロイ、および運用を効率化するための手法とツールの集合であり、ソフトウェア開発のDevOpsに似た概念です。

<a id="ML_DL_TRAIN_EVAL_TrainingError"></a>
## 訓練誤差 | Training Error <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_TrainingError -->
- モデルが<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_TrainingData"> トレーニングデータ </a>セットに対して予測した際の誤差を指し、モデルの学習が進むにつれて通常減少します。

<a id="ML_DL_TRAIN_EVAL_CosineSimilarity"></a>
## コサイン類似度 | Cosine Similarity <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_CosineSimilarity -->
- 二つのベクトルの間の類似度を計算する指標であり、ベクトルのなす角度のコサイン値を用います。

<a id="ML_DL_TRAIN_EVAL_Smoothing"></a>
## スムージング | Smoothing <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Smoothing -->
- データのばらつきを減少させるために使用される手法であり、特に確率分布の推定や時系列データの予測において効果的です。

<a id="ML_DL_TRAIN_EVAL_KLDivergence"></a>
## KL情報量 | Kullback-Leibler Divergence | KL Divergence <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_KLDivergence -->
- 二つの確率分布間の差異を測定する指標であり、情報理論に基づいています。

<a id="ML_DL_TRAIN_EVAL_EarlyStopping"></a>
## Early Stopping <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_EarlyStopping -->
- トレーニング中にモデルの性能が向上しなくなった時点で学習を停止する手法であり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_overfitting"> 過学習 </a>を防ぐのに役立ちます。

<a id="ML_DL_TRAIN_EVAL_ROCCurve"></a>
## ROC曲線 | ROC Curve <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_ROCCurve -->
- モデルの真陽性率と<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_FalsePositive"> 偽陽性 </a>率をプロットしたものであり、モデルの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Classification"> 分類 </a>性能を評価するために使用されます。

<a id="ML_DL_TRAIN_EVAL_Annotation"></a>
## アノテーション | Annotation <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Annotation -->
- データセットに対してラベルやメタデータを付与する作業であり、特に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Supervised"> 教師あり学習 </a>において重要です。

<a id="ML_DL_TRAIN_EVAL_LogitFunc"></a>
## ロジット関数 | Logit Function <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_LogitFunc -->
- ロジスティック<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Regression"> 回帰 </a>モデルにおいて、確率を<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_Odds"> オッズ比 </a>に変換する関数です。

<a id="ML_DL_TRAIN_EVAL_JaccardIndex"></a>
## Jaccard係数 | Jaccard Index <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_JaccardIndex -->
- 二つの集合の交差部分のサイズを和集合のサイズで割ったものであり、類似度を測定する指標です。

<a id="ML_DL_TRAIN_EVAL_tSNE"></a>
## t-SNE | t-Distributed Stochastic Neighbor Embedding | t-SNE <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_tSNE -->
- 高次元データを低次元空間に可視化するための<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_DimReduction"> 次元削減 </a>手法です。

<a id="ML_DL_TRAIN_EVAL_Odds"></a>
## オッズ比 | Odds Ratio <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Odds -->
- ある事象が起きる確率pに対し、p / ( 1 - p)で表される指標

<a id="ML_DL_TRAIN_EVAL_Logit"></a>
## Logit <!-- entry_word_and_anchor:ML_DL_TRAIN_EVAL_Logit -->
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_Odds"> オッズ比 </a>の自然対数をとったもの 
- ある事象が起きる確立pに対しlog(p / (1 - p))で表せ、pを変数とする<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_LogitFunc"> ロジット関数 </a>とも呼ばれる
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_LogitFunc"> ロジット関数 </a>の逆関数がシグモイド関数である。
