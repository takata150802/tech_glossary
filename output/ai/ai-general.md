<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md# -->

## 機械学習 | Machine Learning<a id="5qmf5qKw5a2m57+SIHwgTWFjaGluZSBMZWFybmluZw=="></a>

- 明示的なルール記述なしにデータからパターンを学習するアルゴリズム全般。

## 強化学習 | Reinforcement Learning<a id="5by35YyW5a2m57+SIHwgUmVpbmZvcmNlbWVudCBMZWFybmluZw=="></a>

- エージェントが環境からの報酬を最大化する行動方策を学習。Q学習やポリシー勾配法がある。

## 特徴量 | Feature<a id="54m55b606YePIHwgRmVhdHVyZQ=="></a>

- 学習モデルの入力ベクトルを構成する次元。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5Li75oiQ5YiG5YiG5p6QIHwgUHJpbmNpcGFsIENvbXBvbmVudCBBbmFseXNpcyB8IFBDQQ==">PCA</a>やオートエンコーダーで<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5qyh5YWD5YmK5ribIHwgRGltZW5zaW9uYWxpdHkgUmVkdWN0aW9u">次元削減</a>可能。

## 次元の呪い | Curse of Dimensionality<a id="5qyh5YWD44Gu5ZGq44GEIHwgQ3Vyc2Ugb2YgRGltZW5zaW9uYWxpdHk="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#54m55b606YePIHwgRmVhdHVyZQ==">特徴量</a>の次元を増やしすぎると、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5qmf5qKw5a2m57+SIHwgTWFjaGluZSBMZWFybmluZw==">機械学習</a>モデルの精度が劣化する現象
  - 経験的に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5qmf5qKw5a2m57+SIHwgTWFjaGluZSBMZWFybmluZw==">機械学習</a>モデルの学習に必要なデータ量は<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#54m55b606YePIHwgRmVhdHVyZQ==">特徴量</a>の次元の指数オーダーで増大し、現実的にそのようなデータ量を集めるのが不可能となるため
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#55CD6Z2i6ZuG5Lit54++6LGhIHwgQ29uY2VudHJhdGlvbiBvbiB0aGUgc3BoZXJl">球面集中現象</a>:
    - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#54m55b606YePIHwgRmVhdHVyZQ==">特徴量</a>のノルムが一様となり、意味をなさなくなるため(1万次元の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#54m55b606YePIHwgRmVhdHVyZQ==">特徴量</a>のうち、1番目の次元の値が多少違っても1万次元全体のノルムには全く見えてこない)
    - 標本平均が母平均に一致しなくなるため(1万次元の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#54m55b606YePIHwgRmVhdHVyZQ==">特徴量</a>のうち、1番目の次元の値だけ見ると標本平均は母平均に一致するが(=大数の法則)、1万次元の標本平均と1万次元の母平均のノルムは全く一致しない)

## 球面集中現象 | Concentration on the sphere<a id="55CD6Z2i6ZuG5Lit54++6LGhIHwgQ29uY2VudHJhdGlvbiBvbiB0aGUgc3BoZXJl"></a>

- 次元数の増加に伴い、ある点から見たときの他の点はその点から遠ざかり、また同じような距離に存在するようになる現象。
  - d次元の空間に、ある体積ごとに同じ数の点が分布しているとする
  - この時、ある点を中心として半径がそれぞれrとar(0\<a\<1)のd次元超球S1, S2を考えたとき、(S1の体積 - S2の体積)/(S1の体積)は1 - a^dとなり、dの増加にともない1に近づく
  - つまり、S1の体積のほとんどはS1とS2の超球の隙間に存在する。よって、d次元空間の点もS1とS2の超球の隙間に存在することになる。

## 分類 | Classification<a id="5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24="></a>

- 離散ラベルを予測する<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5pWZ5bir44GC44KK5a2m57+SIHwgU3VwZXJ2aXNlZCBMZWFybmluZw==">教師あり学習</a>問題。多クラスではSoftmaxとクロスエントロピーを使用。

## 回帰 | Regression<a id="5Zue5biwIHwgUmVncmVzc2lvbg=="></a>

- 連続値を予測対象とする<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5pWZ5bir44GC44KK5a2m57+SIHwgU3VwZXJ2aXNlZCBMZWFybmluZw==">教師あり学習</a>。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5pCN5aSx6Zai5pWwIHwgTG9zcyBGdW5jdGlvbg==">損失関数</a>としてMSEやMAEが用いられる。

## 確率的勾配降下法 | SGD<a id="56K6546H55qE5Yu+6YWN6ZmN5LiL5rOVIHwgU0dE"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#44OQ44OD44OB44K144Kk44K6IHwgQmF0Y2ggU2l6ZQ==">バッチサイズ</a>1または小バッチでパラメータ更新を行う<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5Yu+6YWN6ZmN5LiL5rOVIHwgR3JhZGllbnQgRGVzY2VudA==">勾配降下法</a>。計算効率と汎化に優れる。

## 訓練データ | Training Data<a id="6KiT57e044OH44O844K/IHwgVHJhaW5pbmcgRGF0YQ=="></a>

- モデルのパラメータ最適化に使用されるデータセット。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5Lqk5beu5qSc6Ki8IHwgQ3Jvc3MtVmFsaWRhdGlvbg==">交差検証</a>による分割が一般的。

## 訓練誤差 | Training Error<a id="6KiT57e06Kqk5beuIHwgVHJhaW5pbmcgRXJyb3I="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#6KiT57e044OH44O844K/IHwgVHJhaW5pbmcgRGF0YQ==">訓練データ</a>に対する<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5pCN5aSx6Zai5pWwIHwgTG9zcyBGdW5jdGlvbg==">損失関数</a>の平均値。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5rGO5YyW6Kqk5beuIHwgR2VuZXJhbGl6YXRpb24gRXJyb3I=">汎化誤差</a>とのギャップが<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YGO5a2m57+SIHwgT3ZlcmZpdHRpbmc=">過学習</a>の兆候。

## 汎化誤差 | Generalization Error<a id="5rGO5YyW6Kqk5beuIHwgR2VuZXJhbGl6YXRpb24gRXJyb3I="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#6KiT57e044OH44O844K/IHwgVHJhaW5pbmcgRGF0YQ==">訓練データ</a>外の新規入力に対する誤差。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5Lqk5beu5qSc6Ki8IHwgQ3Jvc3MtVmFsaWRhdGlvbg==">交差検証</a>や正則化で抑制。

## F値 | F1 Score<a id="RuWApCB8IEYxIFNjb3Jl"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#6YGp5ZCI546HIHwgUHJlY2lzaW9u">適合率</a>と<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YaN54++546HIHwgUmVjYWxs">再現率</a>の調和平均。不均衡デタにおける<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>性能のバランス指標。

## 混同行列 | Confusion Matrix<a id="5re35ZCM6KGM5YiXIHwgQ29uZnVzaW9uIE1hdHJpeA=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>モデルの性能評価指標。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#6YGp5ZCI546HIHwgUHJlY2lzaW9u">適合率</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YaN54++546HIHwgUmVjYWxs">再現率</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#RuWApCB8IEYxIFNjb3Jl">F値</a>はここから導出。

## 交検証 | Cross Validation<a id="5Lqk5qSc6Ki8IHwgQ3Jvc3MgVmFsaWRhdGlvbg=="></a>

- データを複数分割し、訓練と検証を繰り返すことでモデルの汎化性能を推定する手法。

## 再現率 | Recall<a id="5YaN54++546HIHwgUmVjYWxs"></a>

- 実際の正例のうち、正しく予測された割合。感度とも。

## ROC曲線 | Receiver Operating Characteristic Curve<a id="Uk9D5puy57eaIHwgUmVjZWl2ZXIgT3BlcmF0aW5nIENoYXJhY3RlcmlzdGljIEN1cnZl"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>モデルの閾値を変化させたときのTPRと<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5YG96Zm95oCnIHwgRmFsc2UgUG9zaXRpdmUgfCBGUA==">FP</a>Rの関係を可視化する評価標。

## Jaccard係数 | Jaccard Index<a id="SmFjY2FyZOS/guaVsCB8IEphY2NhcmQgSW5kZXg="></a>

- 集合間の類似度を表す指標で、IoUとも呼ばれる。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#54mp5L2T5qSc5Ye6IHwgT2JqZWN0IERldGVjdGlvbg==">物体検出</a>の評価にも用いられる。

## KL Divergence<a id="S0wgRGl2ZXJnZW5jZQ=="></a>

- ある確率分布が別の分布かられだけ異なるかを測る非対称な距離指標。言語モデルの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJldHJhaW5pbmc=">事前学習</a>にも使用。

## オッズ比 | Odds Ratio<a id="44Kq44OD44K65q+UIHwgT2RkcyBSYXRpbw=="></a>

- 2つの事象の相対的な発生確率比。ロジスティック<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Zue5biwIHwgUmVncmVzc2lvbg==">回帰</a>での係数解釈に用いられる。

## ロジット関数 | Logit Function<a id="44Ot44K444OD44OI6Zai5pWwIHwgTG9naXQgRnVuY3Rpb24="></a>

- 確率値をオッズの対数に変換する写像。ロジスティック<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Zue5biwIHwgUmVncmVzc2lvbg==">回帰</a>の決定関数で使用。

## 尤度 | Likelihood<a id="5bCk5bqmIHwgTGlrZWxpaG9vZA=="></a>

- 観測データの下でのパラメータの確からしさを表す関数。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5pyA5bCk5rOVIHwgTWF4aW11bSBMaWtlbGlob29kIEVzdGltYXRpb24=">最尤法</a>の基礎。

## 最尤法 | Maximum Likelihood Estimation<a id="5pyA5bCk5rOVIHwgTWF4aW11bSBMaWtlbGlob29kIEVzdGltYXRpb24="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5bCk5bqmIHwgTGlrZWxpaG9vZA==">尤度</a>関数を最大化するパラメータ推定法。多くの統計モデルの学習基盤。

## 標本誤差 | Sampling Error<a id="5qiZ5pys6Kqk5beuIHwgU2FtcGxpbmcgRXJyb3I="></a>

- 母集団と標本の間で推定値が異なる誤差。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5Lqk5beu5qSc6Ki8IHwgQ3Jvc3MtVmFsaWRhdGlvbg==">交差検証</a>で統計的に評価可能。

## 標準化 | Standardization<a id="5qiZ5rqW5YyWIHwgU3RhbmRhcmRpemF0aW9u"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#54m55b606YePIHwgRmVhdHVyZQ==">特徴量</a>のスケールを平均0、分散1に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5q2j6KaP5YyWIHwgUmVndWxhcml6YXRpb24=">正規化</a>する前処理。勾配安定性と収束性向上に寄与。

## 次元削減 | Dimensionality Reduction<a id="5qyh5YWD5YmK5ribIHwgRGltZW5zaW9uYWxpdHkgUmVkdWN0aW9u"></a>

- 高次元特徴空間を情報保持しつつ低次元へ射影する処理。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5Li75oiQ5YiG5YiG5p6QIHwgUHJpbmNpcGFsIENvbXBvbmVudCBBbmFseXNpcyB8IFBDQQ==">PCA</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#dC1TTkUgfCB0LURpc3RyaWJ1dGVkIFN0b2NoYXN0aWMgTmVpZ2hib3IgRW1iZWRkaW5n">t-SNE</a>、UMAPなど。

## 正規化 | Regularization<a id="5q2j6KaP5YyWIHwgUmVndWxhcml6YXRpb24="></a>

- モデルの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YGO5a2m57+SIHwgT3ZlcmZpdHRpbmc=">過学習</a>を防ぐため、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5pCN5aSx6Zai5pWwIHwgTG9zcyBGdW5jdGlvbg==">損失関数</a>にペナルティ項を加える手法。L1, L2正則化など。

## 自己組織化マップ | Self-Organizing Map<a id="6Ieq5bex57WE57mU5YyW44Oe44OD44OXIHwgU2VsZi1Pcmdhbml6aW5nIE1hcA=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5pWZ5bir44Gq44GX5a2m57+SIHwgVW5zdXBlcnZpc2VkIExlYXJuaW5n">教師なし学習</a>による高次元データの位相保存写像。Kohonenマップとも。

## 適合率 | Precision<a id="6YGp5ZCI546HIHwgUHJlY2lzaW9u"></a>

- 予測した正例のうち、実際に正しかった割合。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#RuWApCB8IEYxIFNjb3Jl">F値</a>に影響。

## 重回帰 | Multiple Regression<a id="6YeN5Zue5biwIHwgTXVsdGlwbGUgUmVncmVzc2lvbg=="></a>

- 複数の説明変数から連続目的変数を予測する<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Zue5biwIHwgUmVncmVzc2lvbg==">回帰</a>手法。

## EMアルゴリズム | Expectation-Maximization<a id="RU3jgqLjg6vjgrTjg6rjgrrjg6AgfCBFeHBlY3RhdGlvbi1NYXhpbWl6YXRpb24="></a>

- 隠れ変数のある確率モデルのパラメータ推定手法で、EステップとMステップを交互に適用。

## サポートベクターマシン | SVM<a id="44K144Od44O844OI44OZ44Kv44K/44O844Oe44K344OzIHwgU1ZN"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#44Kr44O844ON44Or44OI44Oq44OD44KvIHwgS2VybmVsIFRyaWNr">カーネルトリック</a>を利用して高次元空間でマージン最大化を行う線形<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>器。

## カーネルトリック | Kernel Trick<a id="44Kr44O844ON44Or44OI44Oq44OD44KvIHwgS2VybmVsIFRyaWNr"></a>

- 非線形特徴変換を暗黙的に高次元空間で内計算する手法。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#44K144Od44O844OI44OZ44Kv44K/44O844Oe44K344OzIHwgU1ZN">SVM</a>や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5Li75oiQ5YiG5YiG5p6QIHwgUHJpbmNpcGFsIENvbXBvbmVudCBBbmFseXNpcyB8IFBDQQ==">PCA</a>で活用。

## ランダムフォレスト | Random Forest<a id="44Op44Oz44OA44Og44OV44Kp44Os44K544OIIHwgUmFuZG9tIEZvcmVzdA=="></a>

- 多数の定木をバギングにより構築し、多数決で出力を得るアンサンブル学習法。

## バイアス | Bias<a id="44OQ44Kk44Ki44K5IHwgQmlhcw=="></a>

- モデルの予測値の平均と真の値との差。
- 複雑なモデルを使用すると<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#44OQ44Kk44Ki44K5IHwgQmlhcw==">バイアス</a>は低下するが、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#44OQ44Oq44Ki44Oz44K5IHwgVmFyaWFuY2U=">バリアンス</a>が増加する傾向がある。

## バリアンス | Variance<a id="44OQ44Oq44Ki44Oz44K5IHwgVmFyaWFuY2U="></a>

- モデルの予測値の分散。
- 学習データセットの変動に対するモデルの感度を示す。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#44OQ44Oq44Ki44Oz44K5IHwgVmFyaWFuY2U=">バリアンス</a>が高い場合、単一の学習データセットに<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YGO5a2m57+SIHwgT3ZlcmZpdHRpbmc=">過学習</a>している可能性がある。

## 削減不能な誤差 | Irreducible Error<a id="5YmK5rib5LiN6IO944Gq6Kqk5beuIHwgSXJyZWR1Y2libGUgRXJyb3I="></a>

- データの測定誤差などに由来するノイズの分散。
- 削減できない。
