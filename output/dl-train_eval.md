<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md# -->

## 訓練データ | トレーニングデータ | Training Data<a id="6KiT57e044OH44O844K/IHwg44OI44Os44O844OL44Oz44Kw44OH44O844K/IHwgVHJhaW5pbmcgRGF0YQ=="></a>

- モデルを学習させるために使用されるデータセットで、モデルがデータのパターンを認識し、予測や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>の能力を向上させるために利用されます。

## 過学習 | Overfitting<a id="6YGO5a2m57+SIHwgT3ZlcmZpdHRpbmc="></a>

- モデルが<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#6KiT57e044OH44O844K/IHwg44OI44Os44O844OL44Oz44Kw44OH44O844K/IHwgVHJhaW5pbmcgRGF0YQ==">訓練データ</a>に過度に適合し、新しいデータに対して一般化できない状態を指します。
- 対策として、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#44OJ44Ot44OD44OX44Ki44Km44OIIHwgRHJvcG91dA==">Dropout</a>が有名。

## 交差検証 | Cross-Validation<a id="5Lqk5beu5qSc6Ki8IHwgQ3Jvc3MtVmFsaWRhdGlvbg=="></a>

- データセットを複数の部分に分割してモデルを評価する手法であり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#6YGO5a2m57+SIHwgT3ZlcmZpdHRpbmc=">過学習</a>を防ぎ、モデルの汎化性能を評価するのに役立ちます。

## 損失関数 | Loss Function<a id="5pCN5aSx6Zai5pWwIHwgTG9zcyBGdW5jdGlvbg=="></a>

- モデルの予測と実際の値との間の誤差を計算する関数であり、モデルのパフォーマンスを評価し、最適化するために使用されます。

## word2vec<a id="d29yZDJ2ZWM="></a>

- 単語をベクトル形式で表現する技術であり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5nIHwgTkxQ">自然言語処理</a>において単語間の意味的な類似性を捉えるために使用されます。

## ハイパーパラメータ | Hyperparameter<a id="44OP44Kk44OR44O844OR44Op44Oh44O844K/IHwgSHlwZXJwYXJhbWV0ZXI="></a>

- モデルの学習過程で設定されるパラメータであり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5a2m57+S546HIHwgTGVhcm5pbmcgUmF0ZQ==">学習率</a>や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#44OQ44OD44OB44K144Kk44K6IHwgQmF0Y2ggU2l6ZQ==">バッチサイズ</a>など、モデルの構造やトレーニングに影響を与えます。

## Batch Normalization<a id="QmF0Y2ggTm9ybWFsaXphdGlvbg=="></a>

- 各ミニバッチの平均と分散を<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5qiZ5rqW5YyWIHwgU3RhbmRhcmRpemF0aW9u">標準化</a>することで、学習を安定化させ、トレーニングの速度と性能を向上させる手法です。

## 確率的勾配降下法 | Stochastic Gradient Descent | SGD<a id="56K6546H55qE5Yu+6YWN6ZmN5LiL5rOVIHwgU3RvY2hhc3RpYyBHcmFkaWVudCBEZXNjZW50IHwgU0dE"></a>

- ランダムに選択されたデータポイントに基づいてモデルのパラメータを更新し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5pCN5aSx6Zai5pWwIHwgTG9zcyBGdW5jdGlvbg==">損失関数</a>を最小化する最適化アルゴリズムです。

## ドロップアウト | Dropout<a id="44OJ44Ot44OD44OX44Ki44Km44OIIHwgRHJvcG91dA=="></a>

- トレーニング中にランダムに一部のノードを無効化することで、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#6YGO5a2m57+SIHwgT3ZlcmZpdHRpbmc=">過学習</a>を防ぎ、モデルの汎化性能を向上させる正則化手法です。

## 活性化関数 | Activation Function<a id="5rS75oCn5YyW6Zai5pWwIHwgQWN0aXZhdGlvbiBGdW5jdGlvbg=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>の各ノードの出力に適用される関数であり、非線形性を導入して複雑なパターンを学習するのを助けます。

## Data Augmentation<a id="RGF0YSBBdWdtZW50YXRpb24="></a>

- 既存のデータにランダムな変換（回転、ズーム、反転など）を加えることで、データセットを人工的に拡張し、モデルの汎化性能を向上させる手法です。

## バッチサイズ | Batch Size<a id="44OQ44OD44OB44K144Kk44K6IHwgQmF0Y2ggU2l6ZQ=="></a>

- モデルのトレーニング中に一度に処理されるデータポイントの数を指し、トレーニングの速度と安定性に影響を与えます。

## エポック | Epoch<a id="44Ko44Od44OD44KvIHwgRXBvY2g="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#6KiT57e044OH44O844K/IHwg44OI44Os44O844OL44Oz44Kw44OH44O844K/IHwgVHJhaW5pbmcgRGF0YQ==">トレーニングデータ</a>全体をモデルが一度完全に通過することを指し、モデルがデータセットにどれだけ多くの回数適合されたかを示します。

## TensorFlow<a id="VGVuc29yRmxvdw=="></a>

- Googleが開発したオープンソースのディープラーニングフレームワークであり、さまざまな<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5qmf5qKw5a2m57+SIHwgTWFjaGluZSBMZWFybmluZw==">機械学習</a>モデルの構築とトレーニングに使用されます。

## PyTorch<a id="UHlUb3JjaA=="></a>

- Facebookが開発したオープンソースのディープラーニングフレームワークであり、動的な計算グラフと直感的なAPIを提供し、研究と開発に広く利用されています。

## scikit-learn<a id="c2Npa2l0LWxlYXJu"></a>

- Pythonの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5qmf5qKw5a2m57+SIHwgTWFjaGluZSBMZWFybmluZw==">機械学習</a>ライブラリであり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5Zue5biwIHwgUmVncmVzc2lvbg==">回帰</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#44Kv44Op44K544K/44Oq44Oz44KwIHwgQ2x1c3RlcmluZw==">クラスタリング</a>などの一般的な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5qmf5qKw5a2m57+SIHwgTWFjaGluZSBMZWFybmluZw==">機械学習</a>アルゴリズムを提供します。

## 勾配消失問題 | Vanishing Gradient Problem<a id="5Yu+6YWN5raI5aSx5ZWP6aGMIHwgVmFuaXNoaW5nIEdyYWRpZW50IFByb2JsZW0="></a>

- 深い<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>のトレーニング中に、勾配が小さくなりすぎて更新が効果的に行えなくなる問題。
- 対策として、ReLUやMaxOutなどの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5rS75oCn5YyW6Zai5pWwIHwgQWN0aXZhdGlvbiBGdW5jdGlvbg==">活性化関数</a>の提案

## 誤差逆伝播法 | バックプロパゲーション | Backpropagation<a id="6Kqk5beu6YCG5Lyd5pKt5rOVIHwg44OQ44OD44Kv44OX44Ot44OR44Ky44O844K344On44OzIHwgQmFja3Byb3BhZ2F0aW9u"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>のトレーニングアルゴリズムであり、誤差を出力層から入力層に逆伝播させて、各層の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg==">重み</a>を更新します。

## 学習率 | Learning Rate<a id="5a2m57+S546HIHwgTGVhcm5pbmcgUmF0ZQ=="></a>

- モデルのパラメータを更新する際のステップサイズを決定する<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#44OP44Kk44OR44O844OR44Op44Oh44O844K/IHwgSHlwZXJwYXJhbWV0ZXI=">ハイパーパラメータ</a>であり、学習の収束速度と安定性に影響を与えます。

## Poolingレイヤー | Pooling Layer<a id="UG9vbGluZ+ODrOOCpOODpOODvCB8IFBvb2xpbmcgTGF5ZXI="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#55Wz44G/6L6844G/44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgQ29udm9sdXRpb25hbCBOZXVyYWwgTmV0d29yayB8IENOTg==">畳み込みニューラルネットワーク</a>において、特徴マップの空間次元を縮小し、計算量の削減と特徴の不変性を向上させる層です。

## 混同行列 | Confusion Matrix<a id="5re35ZCM6KGM5YiXIHwgQ29uZnVzaW9uIE1hdHJpeA=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>モデルの性能を評価するための行列であり、真陽性、真陰性、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5YG96Zm95oCnIHwgRmFsc2UgUG9zaXRpdmUgfCBGUA==">偽陽性</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5YG96Zmw5oCnIHwgRmFsc2UgTmVnYXRpdmUgfCBGTg==">偽陰性</a>の数を示します。

## 次元の呪い | Curse of Dimensionality<a id="5qyh5YWD44Gu5ZGq44GEIHwgQ3Vyc2Ugb2YgRGltZW5zaW9uYWxpdHk="></a>

- 高次元データにおいて、データのスパース性や距離計算の信頼性が低下し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5qmf5qKw5a2m57+SIHwgTWFjaGluZSBMZWFybmluZw==">機械学習</a>アルゴリズムの性能が劣化する現象を指します。

## 説明可能なAI | Explainable AI | XAI<a id="6Kqs5piO5Y+v6IO944GqQUkgfCBFeHBsYWluYWJsZSBBSSB8IFhBSQ=="></a>

- モデルの予測や決定の背後にある理由を理解しやすくするための技術や手法の集合であり、透明性と信頼性を向上させます。

## ハルシネーション | Hallucination<a id="44OP44Or44K344ON44O844K344On44OzIHwgSGFsbHVjaW5hdGlvbg=="></a>

- 生成モデルが学習データに存在しない偽の情報を生成する現象を指します。

## F値 | F1 Score<a id="RuWApCB8IEYxIFNjb3Jl"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>モデルの性能を評価する指標であり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#6YGp5ZCI546HIHwgUHJlY2lzaW9u">適合率</a>（<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#6YGp5ZCI546HIHwgUHJlY2lzaW9u">Precision</a>）と<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5YaN54++546HIHwgUmVjYWxs">再現率</a>（<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5YaN54++546HIHwgUmVjYWxs">Recall</a>）の調和平均を取ります。

## 偽陰性 | False Negative | FN<a id="5YG96Zmw5oCnIHwgRmFsc2UgTmVnYXRpdmUgfCBGTg=="></a>

- 実際にはポジティブであるが、モデルがネガティブと誤<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>したデータポイントの数を指します。

## 偽陽性 | False Positive | FP<a id="5YG96Zm95oCnIHwgRmFsc2UgUG9zaXRpdmUgfCBGUA=="></a>

- 実際にはネガティブであるが、モデルがポジティブと誤<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>したデータポイントの数を指します。

## 適合率 | Precision<a id="6YGp5ZCI546HIHwgUHJlY2lzaW9u"></a>

- モデルがポジティブと予測したデータポイントのうち、実際にポジティブである割合を示す指標です。

## 再現率 | Recall<a id="5YaN54++546HIHwgUmVjYWxs"></a>

- 実際にポジティブであるデータポイントのうち、モデルが正しくポジティブと予測した割合を示す指標です。

## MLOps<a id="TUxPcHM="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5qmf5qKw5a2m57+SIHwgTWFjaGluZSBMZWFybmluZw==">機械学習</a>モデルの開発、デプロイ、および運用を効率化するための手法とツールの集合であり、ソフトウェア開発のDevOpsに似た概念です。

## 訓練誤差 | Training Error<a id="6KiT57e06Kqk5beuIHwgVHJhaW5pbmcgRXJyb3I="></a>

- モデルが<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#6KiT57e044OH44O844K/IHwg44OI44Os44O844OL44Oz44Kw44OH44O844K/IHwgVHJhaW5pbmcgRGF0YQ==">トレーニングデータ</a>セットに対して予測した際の誤差を指し、モデルの学習が進むにつれて通常減少します。

## コサイン類似度 | Cosine Similarity<a id="44Kz44K144Kk44Oz6aGe5Ly85bqmIHwgQ29zaW5lIFNpbWlsYXJpdHk="></a>

- 二つのベクトルの間の類似度を計算する指標であり、ベクトルのなす角度のコサイン値を用います。

## スムージング | Smoothing<a id="44K544Og44O844K444Oz44KwIHwgU21vb3RoaW5n"></a>

- データのばらつきを減少させるために使用される手法であり、特に確率分布の推定や時系列データの予測において効果的です。

## KL情報量 | Kullback-Leibler Divergence | KL Divergence<a id="S0zmg4XloLHph48gfCBLdWxsYmFjay1MZWlibGVyIERpdmVyZ2VuY2UgfCBLTCBEaXZlcmdlbmNl"></a>

- 二つの確率分布間の差異を測定する指標であり、情報理論に基づいています。

## Early Stopping<a id="RWFybHkgU3RvcHBpbmc="></a>

- トレーニング中にモデルの性能が向上しなくなった時点で学習を停止する手法であり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#6YGO5a2m57+SIHwgT3ZlcmZpdHRpbmc=">過学習</a>を防ぐのに役立ちます。

## ROC曲線 | ROC Curve<a id="Uk9D5puy57eaIHwgUk9DIEN1cnZl"></a>

- モデルの真陽性率と<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5YG96Zm95oCnIHwgRmFsc2UgUG9zaXRpdmUgfCBGUA==">偽陽性</a>率をプロットしたものであり、モデルの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>性能を評価するために使用されます。

## アノテーション | Annotation<a id="44Ki44OO44OG44O844K344On44OzIHwgQW5ub3RhdGlvbg=="></a>

- データセットに対してラベルやメタデータを付与する作業であり、特に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5pWZ5bir44GC44KK5a2m57+SIHwgU3VwZXJ2aXNlZCBMZWFybmluZw==">教師あり学習</a>において重要です。

## ロジット関数 | Logit Function<a id="44Ot44K444OD44OI6Zai5pWwIHwgTG9naXQgRnVuY3Rpb24="></a>

- ロジスティック<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5Zue5biwIHwgUmVncmVzc2lvbg==">回帰</a>モデルにおいて、確率を<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#44Kq44OD44K65q+UIHwgT2RkcyBSYXRpbw==">オッズ比</a>に変換する関数です。

## Jaccard係数 | Jaccard Index<a id="SmFjY2FyZOS/guaVsCB8IEphY2NhcmQgSW5kZXg="></a>

- 二つの集合の交差部分のサイズを和集合のサイズで割ったものであり、類似度を測定する指標です。

## t-SNE | t-Distributed Stochastic Neighbor Embedding<a id="dC1TTkUgfCB0LURpc3RyaWJ1dGVkIFN0b2NoYXN0aWMgTmVpZ2hib3IgRW1iZWRkaW5n"></a>

- 高次元データを低次元空間に可視化するための<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5qyh5YWD5YmK5ribIHwgRGltZW5zaW9uYWxpdHkgUmVkdWN0aW9u">次元削減</a>手法です。

## オッズ比 | Odds Ratio<a id="44Kq44OD44K65q+UIHwgT2RkcyBSYXRpbw=="></a>

- ある事象が起きる確率pに対し、p / ( 1 - p)で表される指標

## Logit<a id="TG9naXQ="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#44Kq44OD44K65q+UIHwgT2RkcyBSYXRpbw==">オッズ比</a>の自然対数をとったもの
- ある事象が起きる確立pに対しlog(p / (1 - p))で表せ、pを変数とする<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#44Ot44K444OD44OI6Zai5pWwIHwgTG9naXQgRnVuY3Rpb24=">ロジット関数</a>とも呼ばれる
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#44Ot44K444OD44OI6Zai5pWwIHwgTG9naXQgRnVuY3Rpb24=">ロジット関数</a>の逆関数がシグモイド関数である。
