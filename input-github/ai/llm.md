<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md# -->


## 大規模言語モデル| Large Language Model | LLM 
- 大規模な計算資源を使い、一般的にTransformerベースの大規模な言語モデルを、Web上から収集した大規模なテキストデータで学習させたモデル。
  - 2010年代、**主に画像認識や物体検出を行う画像系の深層学習モデルの研究開発が注目を集め、本来ゲーミング用途に使われるGPUが深層学習モデルの研究開発に用いられるようになった(GPGPUの一環)**。その後、Google社主導のTensorFlowやMeta社(旧Facebook社)主導のPyTorchといった深層学習フレームワークがOSSでライセンスの範囲内で自由に利用できることも手伝って、**大規模なGPU計算資源を使った深層学習モデルの学習が様々な研究機関・大学・企業で行われるようになった。**
  - 2017年、**Google社の論文「Attention Is All You Need」にて提唱された自然言語系の深層学習モデルTransformerは、自然言語処理、特に機械翻訳の分野で優れた性能を示し、自然言語処理のおける深層学習のブレイクスルー**となった。この深層学習モデルTransformerの最も重要なアイディアであるアテンション機構は、ほぼ全ての著名なLLMが継承しているアイディアであるので、本論文はLLM分野における基礎的な論文とみなされている。
  - 2018年、OpenAI社の論文「Improving Language Understanding by Generative Pre-Training」で初めて、GPT(=いわゆるLLMの事前学習)が提唱された。従来、自然言語処理系の深層学習モデルは人手でラベル付けしたデータセットで教師あり学習しており、人手でのラベル付けは高コストなため大規模なデータセット構築の制約となっていた。一方で、**GPT(=いわゆるLLMの事前学習)は教師なし学習のためWeb上から収集した膨大なテキストデータを深層学習モデルに学習させることを実現し、大きなブレイクスルー**となった。2022年、OpenAI社がChatGPT(=LLMを用いたChatBotのWebサービス)がリリースされると世間の注目を集め、広く認知されるに至った。2025年現在、北米/中国IT大手が研究開発を牽引し、多くのプロダクト・サービスにLLMが投入され商業的成功を収めている。

**著名なLLM:**
- LLMの研究開発競争は激しく、著名なLLMは日々アップデートが必要なため下記のサーベイ論文、もしくはリーダーボードを参照。
  - サーベイ論文: 
    - Zhao, Wayne Xin, et al. "A survey of large language models." arXiv preprint arXiv:2303.18223 1.2 (2023).　https://arxiv.org/abs/2303.18223
      - 初版version1は2023年3月31日だが、v2,v3...とアップデートされており、version16が2025年3月11日に公開。
      - ※ 下記図は、本サーベイ論文のFigure.3を引用したものです。
        - ![](./llm.md-ASurveyOfLLM_figure3.png)

## リーダーボード | LLMリーダーボード | Leaderboard | LLM Leaderboard
- 主にLLMや画像生成AIの分野で、様々なモデルの性能を客観的に比較・評価するオンラインプラットフォーム
- 具体例:
  - Chatbot Arena: 
    - <a href="https://lmarena.ai/leaderboard">https://lmarena.ai/leaderboard</a>
    - LMArenaによるリーダーボード。
    - **ユーザー投票**でランキングを決める(定量評価も大事だが、ユーザーがどう感じたか?が最も重要というスタンス)。
    - 著名な公開モデルだけでなく、GPT-4oなど**クローズドな商用モデル**もランキングに含まれている。
  - Open LLM Leaderboard: 
    - <a href="https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard">https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard</a>
    - **Hugging Face社による**主に公開モデルのリーダーボード
  - Swallow LLM Leaderboard v2
    - <a href="https://swallow-llm.github.io/evaluation/index.ja.html">https://swallow-llm.github.io/evaluation/index.ja.html</a>
    - 東京科学大学(旧:東工大)岡崎研・横田研 Swallowプロジェクトが、日本語に強いLLMの開発と並行して、公開されているLLMの評価実験を独自に進めているもの。**日本語の**評価タスク定量評価が含まれている。
  - Nejumi LLMリーダーボード3
    - <a href="https://wandb.ai/wandb-japan/llm-leaderboard3/reports/Nejumi-LLM-3--Vmlldzo3OTg2NjM2">https://wandb.ai/wandb-japan/llm-leaderboard3/reports/Nejumi-LLM-3--Vmlldzo3OTg2NjM2</a>
    - WandB社によるリーダーボード。**日本語の**評価タスク定量評価が含まれている。
    - 著名な公開モデルだけでなく、GPT-4oなど**クローズドな商用モデル**もランキングに含まれている。
  - Open Japanese LLM Leaderboard
    - <a href="https://huggingface.co/spaces/llm-jp/open-japanese-llm-leaderboard">https://huggingface.co/spaces/llm-jp/open-japanese-llm-leaderboard</a>
    - LLM-jp によるリーダーボード。 評価ツール llm-jp-eval を活用し、16種類のタスクで日本語の大規模言語モデルを評価している。

## Attention is all you need
- Vaswani, Ashish, et al. "Attention is all you need." Advances in neural information processing systems 30 (2017). https://arxiv.org/abs/1706.03762
- 2017年、Google社の論文
- 本論文にて提唱された自然言語系の深層学習モデルTransformerは、自然言語処理、特に機械翻訳の分野で優れた性能を示し、自然言語処理のおける深層学習のブレイクスルーとなった
- この深層学習モデルTransformerの最も重要なアイディアであるアテンション機構は、ほぼ全ての著名なLLMが継承しているアイディアであるので、本論文はLLM分野における基礎的な論文とみなされている。

## トランスフォーマー | Transformer
- 2017年、Google社の論文「Attention is all you need」にて提唱された自然言語系の深層学習モデル
  - 自然言語処理、特に機械翻訳の分野で優れた性能を示し、自然言語処理のおける深層学習のブレイクスルーとなった
  - 本モデルの最も重要なアイディアであるアテンション機構は、ほぼ全ての著名なLLMが継承している

- Hugging Face社によるOSSの深層学習ライブラリの1つ。
  - 自然言語処理に限らず、コンピュータビジョン、音声処理、マルチモーダルタスクの最先端のモデルの定義、学習、推論に用いられる
  - PyTorch、TensorFlow、JAXといった主要深層学習フレームワークに対応している

## アテンション | アテンション機構 | Attention | Attention mechanism
- 自然言語処理で良く用いられる深層学習モデルの構造の1種。
- 著名な自然言語処理系の深層学習モデルTransformerの最も重要なアイディアで、ほぼ全ての著名なLLMが継承しているアイディアである

- (引用元): <a href="https://speakerdeck.com/chokkan/20230327_riken_llm?slide=14">https://speakerdeck.com/chokkan/20230327_riken_llm?slide=14</a>
  - ![alt text](./llm.md.Transformer_0.png)

## パープレキシティ | Perplexity | 困惑度

- 大規模言語モデルの分野では、**予測精度の指標の1つ**を指し、最もメジャーな指標。
  - ただし **人間との対話品質**や**事実性**を完全には評価できないため、最近は **MT-Bench, AlpacaEval, Chatbot Arena** などの人間評価指標と併用される。
- **ある入力文に対する正解の出力文を**どれだけ「**困惑せずに**」**予測できるか**を示す。
- 直感的には、大規模言語モデルが**次のトークンを予測するときに**「**平均して何通りの選択肢に迷っているか**」を表す。
  - 厳密には、**次のトークンの予測に平均してどれくらいのエントロピー/不確かさがあるか**?を表す。
- **1以上無限大の値を取り、低いほど予測精度が高い良いモデル**。
- 下記数式で定義される。**交差エントロピー誤差のexponentialを取ったものに**等しい。
  - つまり、交差エントロピー誤差はLLMの学習の目的関数と良く用いられ、**学習処理中は学習の進捗状況を表す指標**として、**学習処理後はモデルの良し悪しを表す指標**として用いられるのだが、**パープレキシティとは単にそのexponentialを取ったものに過ぎない**。

$$
\text{PPL}(x_{1:T}) = \exp\left(-\frac{1}{T}\sum_{t=1}^T \log p_\theta(x_t \mid x_{\lt t})\right)
$$

* $T$: シーケンス長
* $p_\theta(x_t \mid x_{<t})$: モデルが次トークン $x_t$ を予測する確率

## 推論 | Inference
- 学習済みモデルを使って、新しい入力に対して出力を生成する処理。
- 大規模言語モデルの分野では、プロンプトを入力に、以下のいずれかを行うことを指す:
  1. 次の1トークンを生成する。
  2. 出力されたトークンを入力プロンプトの末尾に加え、再度次のトークンを生成し、<EOS>が出力されるまで繰り返すテキスト生成。
- 大規模言語モデルの推論の設定パラメータ:
  - 温度 | Temperature
  - Top-k / Top-p 
  - Max tokens

## プロンプト | Prompt
- モデルに与える入力テキスト。タスク指示、質問、文脈、例などを含む。

## デコーダー | Decoder
- シーケンス生成モデルにおける出力系列を逐次生成するモジュール。
- TransformerベースのLLMは、**Encoder-Decoder型**（例: T5）と **Decoder-only型**（例: GPT）に分かれる。

## RMSNorm | Root Mean Square Normalization

- Llama系列のLLMでも採用されている正規化層の1つ。
- Attention is all you needのTransformerで使われていたLayer Normalizationの改良。
  - 分散ではなく二乗平均平方根 (RMS) のみで正規化。
  - xの平均を求める必要がない分、計算量が少ない。

$$
\text{RMSNorm}(x) = \frac{x}{\text{RMS}(x)} \cdot g,
\text{where} \text{RMS}(x) = \sqrt{\frac{1}{d}\sum_{i=1}^d x_i^2 + \epsilon}
$$

* $d$: 次元数
* $g$: 学習可能スケーリング係数

- (引用元): <a href="https://docs.pytorch.org/docs/stable/generated/torch.nn.modules.normalization.RMSNorm.html">https://docs.pytorch.org/docs/stable/generated/torch.nn.modules.normalization.RMSNorm.html</a>

## コンテキスト長 | Context Length | Context Window
- モデルが一度に処理できる**入力トークン列の最大長**。
- LLMの計算量は**コンテキスト長nのとき**$O(n^2)$に比例。
- コンテキスト長が長いほど、長文の理解や生成が可能になるが、計算コストも増大する。

## 自己回帰 | Autoregression
- 過去のトークン系列 $x_{1:t}$ を条件に、次のトークン $x_{t+1}$ を逐次予測する生成方式。

$$
p(x_{1:T}) = \prod_{t=1}^{T} p(x_t \mid x_{\lt t})
$$

## Temperature | 温度パラメータ | 温度
- サンプリング分布のシャープさを制御するパラメータ。
- 対話の創造性・一貫性の調整する。
  - Tが大きいほど多様な応答が生成される。
  - Tが小さいほど決定的な応答が生成される。

$$
p'(x) = \frac{\exp(\log p(x) / T)}{\sum_j \exp(\log p(x_j) / T)}
$$

## FlashAttention
- Self-Attentionを**メモリ効率よくGPUで計算**するアルゴリズム。
  - 行列演算でTilingして(=演算処理を小ブロックに分けて)、メモリアクセス局所性を高めるのと同じように、
  - Softmax演算も工夫してTilingを行っている。
- (参考): GPU と FlashAttension をちゃんと理解したい｜uchiiii <a href="https://zenn.dev/uchiiii/articles/306d0bb7ef67a7">https://zenn.dev/uchiiii/articles/306d0bb7ef67a7</a> 

## Mixture of Experts (MoE)
- LLMのネットワークアーキテクチャの一種。
- 複数の専門家ネットワーク（Expert）を用意し、入力ごとに一部のみを動的に活性化させる。
- 追加のコストを抑えつつLLMのパラメータ総数を増やすための工夫。
- メリット:
  - 計算効率の改善。パラメータ÷{学習/推論に必要な計算量}を低減できる。
- デメリット:
  - 学習の安定性。学習中、活性化されるExpertが偏ると上手く学習できない。

## Self-Attention | 自己注意機構
- 入力トークン列内の各トークン同士が相互に関連度を計算し、重み付き和を取る機構。

$$
\text{Self-Atten}(Q,K,V) = \text{softmax}\left(\frac{QK^\top}{\sqrt{d_k}}\right)V
, \text{where } Q=W_Qx, K=W_Kx, V=W_Vx
$$

* $n$: コンテキスト長
* $d_k$: モデルの次元数
* $x$: 入力トークン列(サイズ: $n \times d_k$)
* $Q$: Query行列(サイズ:$n \times d_k$), $W_{Q}x$で計算される
* $K$: Key行列(サイズ:$n \times d_k$), $W_{K}x$で計算される
* $V$: Value行列(サイズ:$n \times d_k$), $W_{K}x$で計算される
* $QK^\top$: Attention行列(サイズ:$n \times n$)