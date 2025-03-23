<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md# -->

## 人工知能 | Artificial Intelligence | AI　
- 人間の知的な行動を模倣するコンピュータシステム
- 2010代~2024年現在まで続くAIブームは第3次AIブーム(3rd Wave)とされている。
  - First Wave (1950s-1970s):
    - GOFAI（Good Old Fashioned AI；古き良き人工知能）
    - 現在に至るAI研究の基礎となるフレームワークが輩出:
      - シンボリックAIの一般問題解決器GPS（General
Problem Solver）
      - ニューラルネットワークにおけるパーセプトロン
        - 引用元: https://ja.wikipedia.org/wiki/甘利俊一
          - `甘利俊一は連続体力学、情報理論、ニューラルネットワークなどを研究してきた。1967年、多層パーセプトロンの確率的勾配降下法を考えて定式化に成功したが、この早すぎた発見は当時の計算機の能力の低さもあり検証が難しく、あまり注目されずに終わった。しかし、1986年にデビッド・ラメルハート、ジェフリー・ヒントン、ロナルド・J・ウィリアムスが、この方法を再発見し、誤差逆伝播法として発表した事で、ニューラルネットワーク研究の第2次ブームへと繋がっている。勾配消失問題などの技術的困難があり、この第2次ブームは終焉を迎えたが、その後のディープラーニングブームへと続く礎にもなった。` <!-- substituteinhibit -->
      - フレーム問題
      - 意味ネットワーク, フレーム理論
      - ファジー集合
      - 自然言語処理システム SHRDLU
      - 人工無能システム ELIZA
      - 人工知能用プログラミング言語 LISP
      - 第1回人工知能国際会議 IJCAI 1969 @ワシントン 
    - この後最初の「AI の冬」時代へ
  - Second Wave (1980s-1990s):
    - 人間の専門家の知識を持った AI が専門家のような推論を行うエキスパートシステム（Expert System）
      - 人間の専門家の知識を引き出すタスクは知識エンジニアリングと呼ばれ，知識エンジニアという職業まで生まれた
    - 病気の診断を行う MYCIN（マイシン）
    - 油田の推定を行うディップメーターアドバイザー
    - コンピュータの構成を行う XCON（エックスコン）
    - 日本 通産省: 第五世代コンピュータプロジェクト,1982年~
      - 引用元: https://museum.ipsj.or.jp/computer/other/0002.html
        - `通産省は1982年に第五世代コンピュータプロジェクトをスタートさせた．このプロジェクトは，国際貢献を果たしつつ技術先進国として発展するという我が国の政策のもとに始められたもので，国際的にみても創造的・先駆的な技術という意味を込めて「第五世代コンピュータ」と名付けられた．技術目標を「知識情報処理を指向した新しいコンピュータ技術の研究開発」と定め，推進母体として新世代コンピュータ技術開発機構（ICOT）が設立され，技術目標に含まれる多くの要素技術の実証・評価を行うために，並列推論型コンピュータのプロトタイプシステムの試作が行われた．このシステムは，知識情報処理指向のコンピュ−タとしては，世界最高速，かつ，最大規模のものであった．このシステムは，並列推論マシン（PIM）と呼ばれる大規模な並列ハードウェアシステムを持ち，PIM は512台の要素プロセッサからなるPIM/pや256台の要素プロセッサを持つPIM/mなど5つのモデルが作られた．11年間で約540億を投じ1992年度をもって終了した．現在，PIM/pおよびPIM/mは国立科学博物館で保存されている．また，下記のWebで「第五世代博物館」が公開されている．` <!-- substituteinhibit -->
    - 暗黙知の顕在化によるエキスパートシステムの限界などにより，15 年に及ぶ AI 冬の時代へ。この間における主要な進歩は下記の通り：
      - ベイジアンネットワーク | Bayesian Network
      - 遺伝的アルゴリズム | Genetic Algorithm
      - 遺伝的プログラミング  | Genetic Programming
      - マルチエージェントシステム | Multi-agent System
      - 強化学習
      - 統計的機械学習, サポ―トベクターマシン
      - データマイニング | Data Minig
  - Third Wave (2010s-Present):
    - コンピューター ハードウェアの進歩(とGPGPUの活用)と大規模なデータセットによるDeep Learningのブレークスルー
      - 画像認識コンペティションILSVRC2012でトロント大のAlexNetがエラー率 15.3% で優勝し、次点よりも 10.8% 以上低くDeep Learningが広く認知されるきっかけとなった。
        - `Krizhevsky, Alex, Ilya Sutskever, and Geoffrey E. Hinton. "ImageNet classification with deep convolutional neural networks." Communications of the ACM 60.6 (2017): 84-90.` <!-- substituteinhibit -->
        - ILSVRC2012の次点は東大知能機械 原田研究室の牛久祥孝氏。「ヒントンに敗れた男」として日本経済新聞の記事で紹介されるもお名前がtypo…
    - Google、Meta(旧Facebook)、Microsoft、Amazon等の北米IT大手が研究開発を牽引し、多くのプロダクト・サービスにAIが投入され商業的成功を収めている

## 機械学習 | Machine Learning 
- データからパターンを学習し、予測や意思決定を行うアルゴリズムや手法のことです。

## 教師あり学習 | Supervised Learning  
- 入力データとそれに対応する正解ラベルを用いてモデルを訓練する学習方法です。

## 教師なし学習 | Unsupervised Learning  
- ラベルのないデータからパターンや構造を見つけ出す学習方法です。

## 強化学習 | Reinforcement Learning  
- エージェントが環境との相互作用を通じて報酬を最大化する行動を学習する方法です。

## 分類 | Classification  
- データをあらかじめ定義されたカテゴリに分類する機械学習タスクです。

## 回帰 | Regression  
- 連続値を予測する機械学習タスク

## 重回帰 | Multiple Regression  
- 複数の独立変数を用いて従属変数を予測する回帰分析の一種

## サポートベクターマシン | Support Vector Machine | SVM 
- データポイントを分離する最適なハイパープレーンを見つける分類アルゴリズムです。

## クラスタリング | Clustering  
- データを類似したグループ（クラスタ）に分ける教師なし学習の手法です。

## 主成分分析 | Principal Component Analysis | PCA 
- 高次元データを低次元に変換する次元削減の手法です。

## 次元削減 | Dimensionality Reduction  
- 高次元データをより少ない次元に圧縮して、情報の損失を最小限に抑える手法です。

## 最小2乗法 | Least Square Method  
- 目的変数Yを説明変数Xの線形モデルで表したときの２乗誤差(=\epsilon^2)を最小にするパラメータ\thetaを求める手法
- 線形モデルの誤差\epsilonを多変量正規分布と仮定したときの最尤法に相当する

```math
線形モデル: Y = X\theta + \epsilon \\ 
目的変数: Y \\
説明変数: X \\
パラメータ: \theta \\
誤差: \epsilon \\
推定値: \hat{\theta} = (X^TX)^{-1}X^TY ・・・①
```
- ① 推定値 \hat{\theta}の導出:
```math
\epsilon^2 =(Y-X\theta)^T(Y-X\theta)
=Y^TY - Y^TX\theta - \theta^TX^TY + \theta^TX^TX\theta \\
\frac{\partial }{\partial \theta} \epsilon^2 = \frac{\partial }{\partial \theta} Y^TY - \frac{\partial }{\partial \theta} Y^TX\theta - \frac{\partial }{\partial \theta} \theta^TX^TY + \frac{\partial }{\partial \theta} \theta^TX^TX\theta \\
= 0 + \frac{\partial }{\partial \theta} Y^TX\theta - \frac{\partial }{\partial \theta} (X^TY)^T\theta + \frac{\partial }{\partial \theta} \theta^TX^TX\theta \\
= -2 \frac{\partial }{\partial \theta} Y^TX\theta + \frac{\partial }{\partial \theta} \theta^TX^TX\theta ・・・② \\
= -2X^TY+2X^TX\theta ・・・③ \\
```

したがって、\frac{\partial }{\partial \theta} \epsilon^2 = 0となるような\thetaは、
```math
0 = -2X^TY+2X^TX\theta \\
X^TX\theta = X^TY \\
(X^TX)^{-1}X^TX\theta = (X^TX)^{-1}X^TY \\
\theta = (X^TX)^{-1}X^TY ・・・上述の①の式
```

なお②から③の式変形は、
```math
第１項: - 2\frac{\partial }{\partial \theta} Y^TX\theta = - 2 (Y^TX)^T = -2 X^TY \\
第2項: \frac{\partial }{\partial \theta} \theta^TX^TX\theta = 2X^TX\theta 
```


## 最尤法 | Maximum Likelihood Method | MLE 
- 訓練サンプル集合が生じる確率(=尤度)を最大にするパラメータ値を，パラメータの推定量とする方法
- (あとで書く) 最尤法は分布との距離をKLダイバージェンスで測ったときの真の分布に最も近いモデルを推定している https://ibisforest.org/index.php?%E6%9C%80%E5%B0%A4%E6%8E%A8%E5%AE%9A
- (あとで書く) 線形回帰における誤差項が正規分布にしたがうことを仮定してパラメータを推定すると、最尤法と最小二乗法は同一の推定量を与えます。 https://qiita.com/nakey_tdse/items/05a0f1458089818b349d

## 尤度 | Likelihood 
- 訓練サンプルX= {x_1,...,x_n}が与えられたとき、パラメータ 𝜃の下でのデータの発生確率

```math
尤度(または尤度関数): L(X;\theta) = \Pi_{i=1}^Nf(x_i;\theta) <!-- substituteinhibit -->
訓練サンプルの確立モデル: f(x_i;\theta)
```

## 正規化 | Normalization 
- データの[最小値, 最大値]が[0, 1] や[-1, 1]あるいは[0,255] となるように変換するといった、後続の計算処理に都合が良いようにデータをスケーリングすること

## 標準化 | Standardization 
- データの平均が0, 分散が1となるように変換すること

## コンピュータビジョン | Computer Vision | CV 
- 画像や動画から有用な情報を抽出する技術分野です。

## セグメンテーション | Segmentation  
- 画像をピクセル単位でカテゴリに分けるプロセスです。

## 特徴量 
- 生データの性質や意味を良く表現し、後続の計算処理に利用しやすい形式に変換されたデータ。

## 物体検出 | Object Detection  
- 画像内の複数の物体を検出し、その位置とカテゴリを特定する技術です。

## 自然言語処理 | Natural Language Processing | NLP 
- 人間の言語を理解し、生成するコンピュータの能力を研究する分野です。

## 音声認識 | Speech Recognition  
- 音声信号をテキストに変換する技術です。

## k-means  
- データをk個のクラスタに分けるクラスタリングアルゴリズムです。

## カーネルトリック | Kernel Trick  
- 非線形データを線形に分離可能な高次元空間に変換する手法です。

## ランダムフォレスト | Random Forest  
- 複数の決定木を組み合わせて予測を行うアンサンブル学習アルゴリズムです。

## 自己組織化マップ | Self-Organizing Map | SOM 
- 高次元データを低次元空間にマッピングする教師なし学習のニューラルネットワークです。

## 汎化誤差 | Generalization Error 

- 訓練データに無いサンプルに対する誤差
- 以下3つから構成されるものと考える
  - バイアス誤差
  - バリアンス誤差
  - ノイズ ・・・モデル集合の選択に依存せず，本質的に減らせない真のモデルのばらつき

## 標本誤差 | Sample Error  

- 訓練データのサンプルに対する誤差
- 「経験誤差 | empirical error」や「経験損失 | empirical risk」ともいう
```math
標本誤差: R_{emp}(\theta) = 1/N \sigma_{i=1}^{N}L(x_i,\theta) \\
損失関数: L(x,\theta) \\
データ: D={x_1,...,x_N} 
```
## バイアス誤差 | Bias Error  
- 候補モデル集合に真のモデルは含まれないことで生じる誤差

## バリアンス誤差 | Variance Error 
- 訓練データが異なると，異なる予測モデルが選択されることで生じる誤差

# 参考文献
- 朱鷺の杜Wiki https://ibisforest.org/index.php?FrontPage
- https://www.kamishima.net/archive/mldm-overview.pdf
- https://www.ieice-hbkb.org/files/S3/S3gun_03hen_01.pdf
- https://twitter.com/losnuevetoros/status/1168326617023700992
