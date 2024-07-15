<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md# -->

<a id="ML_DL_DeepLearing_"></a>
## 深層学習 | Deep Learning <!-- entry_word_and_anchor:ML_DL_DeepLearing_ -->
- 複数の層を持つ<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_Neural_Network"> ニューラルネットワーク </a>を使用してデータから特徴を自動的に学習する<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_ML"> 機械学習 </a>の一分野です。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_DeepLearing_"> Deep Learning </a> is a subfield of machine learning that uses neural networks with multiple layers to automatically learn features from data.

<a id="ML_DL_Neural_Network"></a>
## ニューラルネットワーク | Neural Network <!-- entry_word_and_anchor:ML_DL_Neural_Network -->
- 単純パーセプトロン,ロジスティック<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Regression"> 回帰 </a>を多層にしたもの。
  - 多層にすることで線形分離可能でない問題を解くことができるようになった。
  - 課題は<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_Neural_Network"> ニューラルネットワーク </a>の学習の手法であったが、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_BackProp"> 誤差逆伝播法 </a>が提唱され(1986年)、2010年代の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_DeepLearing_"> Deep Learning </a>で広く用いられることとなった。
- シグモイド関数の代わりに別の非線形関数を用いることも多く、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#ML_DL_TRAIN_EVAL_ActivationFunc"> 活性化関数 </a>と呼ばれる。




<a id="ML_DL_CNN"></a>
## 畳み込みニューラルネットワーク | Convolutional Neural Network | CNN <!-- entry_word_and_anchor:ML_DL_CNN -->
- 画像処理に特化した<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_Neural_Network"> ニューラルネットワーク </a>であり、空間的な特徴を捉えるために畳み込み層を使用します。

<a id="ML_DL_RNN"></a>
## リカレントニューラルネットワーク | Recurrent Neural Network | RNN <!-- entry_word_and_anchor:ML_DL_RNN -->
- 時系列データやシーケンスデータを処理するために、出力を次の入力としてフィードバックする構造を持つ<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_Neural_Network"> ニューラルネットワーク </a>です。

<a id="ML_DL_LSTM"></a>
## Long Short-Term Memory | LSTM <!-- entry_word_and_anchor:ML_DL_LSTM -->
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_RNN"> リカレントニューラルネットワーク </a>の一種であり、長期間の依存関係を持つデータを効率的に学習することができます。

<a id="ML_DL_GAN"></a>
## 敵対的生成ネットワーク | Generative Adversarial Network | GAN <!-- entry_word_and_anchor:ML_DL_GAN -->
- 生成モデルと識別モデルが競い合うことで高品質なデータを生成するモデルです。

<a id="ML_DL_DeepFake"></a>
## Deepfake <!-- entry_word_and_anchor:ML_DL_DeepFake -->

<a id="ML_DL_Sep2Sep"></a>
## Seq2Seq Model | Sequence-to-Sequence Model <!-- entry_word_and_anchor:ML_DL_Sep2Sep -->

<a id="ML_DL_VAE"></a>
## 変分オートエンコーダー | Variational Autoencoder | VAE <!-- entry_word_and_anchor:ML_DL_VAE -->
- データの潜在変数を学習し、新しいデータの生成や再構成を行う生成モデルの一種です。

<a id="ML_DL_TransferLearning"></a>
## 転移学習 | Transfer Learning <!-- entry_word_and_anchor:ML_DL_TransferLearning -->

<a id="ML_DL_fine_tuning"></a>
## fine-Tuning <!-- entry_word_and_anchor:ML_DL_fine_tuning -->

<a id="ML_DL_QLearning"></a>
## Q-Learning <!-- entry_word_and_anchor:ML_DL_QLearning -->
- エージェントが環境からの報酬に基づいて最適な行動を学習する<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_Reinforcement"> 強化学習 </a>アルゴリズムです。

<a id="ML_DL_Attention"></a>
## アテンション機構 | Attention Mechanism <!-- entry_word_and_anchor:ML_DL_Attention -->

<a id="ML_DL_Transformer"></a>
## トランスフォーマー | Transformer <!-- entry_word_and_anchor:ML_DL_Transformer -->
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_Attention"> アテンション機構 </a>を用いて<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#ML_ML_OVERVIEW_NLP"> 自然言語処理 </a>において高い性能を発揮するモデルです。

<a id="ML_DL_DQN"></a>
## Deep Q-Network | DQN <!-- entry_word_and_anchor:ML_DL_DQN -->
- ディープラーニングを用いた<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#ML_DL_QLearning"> Q-Learning </a>の実装であり、エージェントが複雑な環境で最適な行動を学習するために使用されます。

<a id="ML_DL_OneShotLearnig"></a>
## One-shot Learning <!-- entry_word_and_anchor:ML_DL_OneShotLearnig -->
- 少ないサンプルで学習を行うことができる技術です。

<a id="ML_DL_ZeroShotLearnig"></a>
## Zero-shot Learning <!-- entry_word_and_anchor:ML_DL_ZeroShotLearnig -->
- 学習に使用していないクラスを識別することができる技術です。

<a id="ML_DL_PromptEngineering"></a>
## プロンプトエンジニアリング | Prompt Engineering <!-- entry_word_and_anchor:ML_DL_PromptEngineering -->
- 生成モデルに対する入力（プロンプト）を最適化して望ましい出力を得る技術です。

<a id="ML_DL_EMAlgo"></a>
## EMアルゴリズム | Expectation-Maximization Algorithm | EM Algorithm <!-- entry_word_and_anchor:ML_DL_EMAlgo -->

<a id="ML_DL_DiffusionModel"></a>
## 拡散モデル | Diffusion Model <!-- entry_word_and_anchor:ML_DL_DiffusionModel -->
