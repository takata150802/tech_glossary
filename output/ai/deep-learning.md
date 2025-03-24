<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md# -->

## 重み | 重みパラメータ | Weight | Weight Parameter<a id="6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg=="></a>

- モデル内部で学習される<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg==">重み</a>およびバイアスで、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6Kqk5beu6YCG5Lyd5pKt5rOVIHwg44OQ44OD44Kv44OX44Ot44OR44Ky44O844K344On44OzIHwgIEJhY2twcm9wYWdhdGlvbg==">誤差逆伝播法</a>で最適化される対象。

## ファインチューニング | Fine-tuning | Fine tuning<a id="44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmcgfCBGaW5lIHR1bmluZw=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJldHJhaW5pbmc=">事前学習</a>済みモデルに対し、特定のタスクやドメインに合わせて勾配更新を行うトレーニング。

## 学習率 | Learning Rate<a id="5a2m57+S546HIHwgTGVhcm5pbmcgUmF0ZQ=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5Yu+6YWN6ZmN5LiL5rOVIHwgR3JhZGllbnQgRGVzY2VudA==">勾配降下法</a>において、各ステップでパラメータをどれだけ更新するかを制御する<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OP44Kk44OR44O844OR44Op44Oh44O844K/IHwgSHlwZXJwYXJhbWV0ZXI=">ハイパーパラメータ</a>。

## 自己教師あり学習 | Self-supervised Learning<a id="6Ieq5bex5pWZ5bir44GC44KK5a2m57+SIHwgU2VsZi1zdXBlcnZpc2VkIExlYXJuaW5n"></a>

- ラベルなしデータから部分的にタスクを構成し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5pWZ5bir44GC44KK5a2m57+SIHwgU3VwZXJ2aXNlZCBMZWFybmluZw==">教師あり学習</a>のように学習する手法。

## 勾配降下法 | Gradient Descent<a id="5Yu+6YWN6ZmN5LiL5rOVIHwgR3JhZGllbnQgRGVzY2VudA=="></a>

- 誤差関数の勾配を計算し、負の方向へパラメータを更新する最適化アルゴリズム。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OQ44OD44OB44K144Kk44K6IHwgQmF0Y2ggU2l6ZQ==">バッチサイズ</a>に応じて<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#56K6546H55qE5Yu+6YWN6ZmN5LiL5rOVIHwgU0dE">SGD</a>、Mini-batch、Full-batchなどに分かれ、変種としてAdamやRMSpropがある。

## Poolingレイヤー | Pooling layer<a id="UG9vbGluZ+ODrOOCpOODpOODvCB8IFBvb2xpbmcgbGF5ZXI="></a>

- 畳み込み後の特徴マップを空間的にダウンサンプリングする操作。MaxPoolingやAveragePoolingが主流。

## エポック | Epoch<a id="44Ko44Od44OD44KvIHwgRXBvY2g="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#6KiT57e044OH44O844K/IHwgVHJhaW5pbmcgRGF0YQ==">訓練データ</a>全体を1回通して学習するサイクル。過学回避のため早期終了と併用。

## ドロップアウト | Dropout<a id="44OJ44Ot44OD44OX44Ki44Km44OIIHwgRHJvcG91dA=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YGO5a2m57+SIHwgT3ZlcmZpdHRpbmc=">過学習</a>防止のために、学習時ランダムにユニットを無効化する正則化手法。

## ハイパーパラメータ | Hyperparameter<a id="44OP44Kk44OR44O844OR44Op44Oh44O844K/IHwgSHlwZXJwYXJhbWV0ZXI="></a>

- 訓練前に設定する調整変数で、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OQ44OD44OB44K144Kk44K6IHwgQmF0Y2ggU2l6ZQ==">バッチサイズ</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5a2m57+S546HIHwgTGVhcm5pbmcgUmF0ZQ==">学習率</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OJ44Ot44OD44OX44Ki44Km44OIIHwgRHJvcG91dA==">ドロップアウト</a>率などが含まれる。

## バッチサイズ | Batch Size<a id="44OQ44OD44OB44K144Kk44K6IHwgQmF0Y2ggU2l6ZQ=="></a>

- 1回のパラメータ更新に使うサンプル数。メモリ使用と学習安定性に影響。

## バリアンス誤差 | Variance Error<a id="44OQ44Oq44Ki44Oz44K56Kqk5beuIHwgVmFyaWFuY2UgRXJyb3I="></a>

- 学習データのわずかな変化に対して予測結果が大きく変動する傾向。高容量モデルで顕著。

## リカレントニューラルネットワーク | RNN<a id="44Oq44Kr44Os44Oz44OI44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgUk5O"></a>

- 系列データに適したネットワークで、隠れ状態を時間的に伝播。勾配消失の影響を受けやすい。

## 勾配消失問題 | Vanishing Gradient Problem<a id="5Yu+6YWN5raI5aSx5ZWP6aGMIHwgVmFuaXNoaW5nIEdyYWRpZW50IFByb2JsZW0="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5rS75oCn5YyW6Zai5pWwIHwgQWN0aXZhdGlvbiBGdW5jdGlvbg==">活性化関数</a>や深い層の影響で勾配が消失し、学習が進行しなくなる現象。ReLUや残差接続で緩和可能。

## 変分オートエンコーダー | VAE<a id="5aSJ5YiG44Kq44O844OI44Ko44Oz44Kz44O844OA44O8IHwgVkFF"></a>

- 潜在変数モデルを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>で構成し、ELBOの最小化により訓練される生成モデル。

## 拡散モデル | Diffusion Model<a id="5ouh5pWj44Oi44OH44OrIHwgRGlmZnVzaW9uIE1vZGVs"></a>

- ノイズ付加と復元の2過程でデータ生成を行う確率的生成モデル。DDPMやStable Diffusionが代表。

## 損失関数 | Loss Function<a id="5pCN5aSx6Zai5pWwIHwgTG9zcyBGdW5jdGlvbg=="></a>

- モデル出力と教師信号との誤差を数値化する指標で、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5Yu+6YWN6ZmN5LiL5rOVIHwgR3JhZGllbnQgRGVzY2VudA==">勾配降下法</a>の最小化対象。代表例にクロスエントロピーやMSE。

## 教師あり学習 | Supervised Learning<a id="5pWZ5bir44GC44KK5a2m57+SIHwgU3VwZXJ2aXNlZCBMZWFybmluZw=="></a>

- 入力と正解ラベルの対を用いた学習手法。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Zue5biwIHwgUmVncmVzc2lvbg==">回帰</a>が該当。

## 敵対的生成ネットワーク | GAN<a id="5pW15a++55qE55Sf5oiQ44ON44OD44OI44Ov44O844KvIHwgR0FO"></a>

- 生成器と識別器がミニマックスゲームを行う構造を持つ生成モデル。潜在空間から高品質サンプル生成が可能。

## 物体検出 | Object Detection<a id="54mp5L2T5qSc5Ye6IHwgT2JqZWN0IERldGVjdGlvbg=="></a>

- 画像内の対象物を局所化（バウンディングボックス）し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>も行う複合タスク。YOLOやFaster R-<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#55Wz44G/6L6844G/44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgQ05O">CNN</a>が代表。

## 畳み込みニューラルネットワーク | CNN<a id="55Wz44G/6L6844G/44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgQ05O"></a>

- 空間的局所性とパラメータ共有を活用し、画像や時系列データの処理に特化したディープネットワーク。

## 自然言語処理 | NLP<a id="6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQ"></a>

- 言語的構造を持つ非構造データを扱う<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5qmf5qKw5a2m57+SIHwgTWFjaGluZSBMZWFybmluZw==">機械学習</a>分野。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>化、エンベディング、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwgQXR0ZW50aW9u">Attention</a>機構を含む。

## 誤差逆伝播法 | バックプロパゲーション | Backpropagation<a id="6Kqk5beu6YCG5Lyd5pKt5rOVIHwg44OQ44OD44Kv44OX44Ot44OR44Ky44O844K344On44OzIHwgIEJhY2twcm9wYWdhdGlvbg=="></a>

- チェインルールにより勾配を層ごとに計算し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg==">重み</a>更新に利用。

## 転移学習 | Transfer Learning<a id="6Lui56e75a2m57+SIHwgVHJhbnNmZXIgTGVhcm5pbmc="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJldHJhaW5pbmc=">事前学習</a>済みモデルの知識を別タスクに応用する学習パラダイム。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmcgfCBGaW5lIHR1bmluZw==">ファインチューニング</a>と併用。

## 過学習 | Overfitting<a id="6YGO5a2m57+SIHwgT3ZlcmZpdHRpbmc="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#6KiT57e06Kqk5beuIHwgVHJhaW5pbmcgRXJyb3I=">訓練誤差</a>が小さいが<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5rGO5YyW6Kqk5beuIHwgR2VuZXJhbGl6YXRpb24gRXJyb3I=">汎化誤差</a>が大きい状態。正則化やデータ拡張で緩和可能。

## 音声認識 | ASR<a id="6Z+z5aOw6KqN6K2YIHwgQVNS"></a>

- 音響<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#54m55b606YePIHwgRmVhdHVyZQ==">特徴量</a>から系列ラベル（文字列）への変換問題。典型的にはCTC損失や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44Oq44Kr44Os44Oz44OI44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgUk5O">RNN</a>-Tを使用。
