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
      - ※ 下記図は、本サービス論文のFigure.3を引用したものです。
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

## 推論 | Inference	
- 学習済みモデルに対してプロンプトを与え、次のトークンまたはテキスト全体を生成させる処理。

## プロンプト | Prompt
- モデルへの入力文。コンテキストや命令、質問などを含むことが多く、Zero-shotやFew-shotにも活用される。

## デコーダー | Decoder
- Transformerにおける出力生成側のネットワーク構造で、自己回帰的にトークンを予測する。

## RMSNorm | LayerNorm
- 各レイヤーにおいて出力のスケーリングを正規化し勾配の安定性を高めるテクニック。

## 位置エンコーディング | Positional Encoding
- トークンの系列順序情報をモデルに与えるための埋め込み。絶対位置または相対位置を採用。

## アテンション | Attention
- 各トークンが他のトークンとの関連性を計算するメカニズム。Self-AttentionがTransformerの要。

## 自己回帰 | Autoregressive
- 入力の過去のトークンを使って次のトークンを逐次生成するモデル構造。GPT系列などが該当。

## コンテキスト長 | Context Length | Context Window
- モデルが一度に処理可能な最大トークン数。大きいほど長文処理能力が向上するが、アテンションの計算量が増大する。

## Temperature
- モデルの出力の多様性を制御するパラメータ。高い値（例：1.0）は多様な応答を生成し、低い値（例：0.2）はより決定的な応答を生成する。
- 例：ChatGPTの温度パラメータを調整することで、よりクリエイティブな応答や、より一貫性のある応答を生成することができる。

## FlashAttention
- アテンション計算をメモリアクセス最適化により高速化したアルゴリズム。Transformerのスケーラビリティを改善。

## Mixture of Experts | MoE
- 複数のサブネットワーク（専門家）を用意し、入力ごとに一部のみを動かすことで、計算量を抑えつつモデルの能力を拡張。

## Sparse Transformer
- 全トークン間のアテンションではなく、一部の接続のみ有効にすることで、計算量とメモリ使用を削減したTransformerの変種。

## トークン | Token
- モデルの入出力単位であり、BPEやSentencePieceなどのサブワード分割により生成される。

## トークナイザー | トークナイザ | Tokenizer
- 生テキストをサブワード単位のトークン列に変換する処理器で、エンコーディングとデコーディングを担う。

## エンべディング | Embedding
- 離散トークンを連続値ベクトル空間へ写像する手法。語彙空間のワンホットベクトルを低次元密ベクトルに変換し、意味的距離の保存を目指す。
- 通常は入力エンべディングと位置エンべディングの加算で初期入力が構成される。

## Self-Attention
- 入力系列内の全トークンペアに対し、クエリ（Q）、キー（K）、バリュー（V）の内積スコアをSoftmax正規化して加重和を取るアテンション機構。Transformerの基盤であり、長距離依存関係の獲得に寄与する。

## SentencePiece 
- トークン化を言語非依存に行うためのサブワード単位トークナイザー。Unigram Language ModelまたはBPEに基づき、語彙と分割境界を学習する。スペースを専用トークンとして扱うことで前処理不要。

## BPE | Byte Pair Encoding
- 頻出ペアのマージ操作を繰り返して語彙を構成するデータ圧系サブワード分割アルゴリズム。単語の分割可能性を保ちつつ、語彙サイズと未出語処理のトレードオフを実現。

## コサイン類似度 | Cosine Similarity
- ベクトル間の角度のコサイン値で類似度を測定。エンベディング間比較に使用。	

## コーパス | Corpus
- テキストデータのデータセット。
- 自然言語処理の分野で、解析対象となる文書群全体のこと。

## 語彙 | Vocabulary
- コーパス内に現れる全ての単語を集めたもの

## 単語袋モデル | Bag of Words | BoW

- 情報検索の分野で、ある文章をベクトルで表現するための手法の一種。
- ある文章$d$に対して、語彙に含まれる単語の出現回数をカウントし、それを以ってその文章$d$を表すベクトルする。
- 語順は考慮されない。
- 具体例: 
  - (引用元): <a href="https://qiita.com/kazukiii/items/d717add45bbc76a71430">https://qiita.com/kazukiii/items/d717add45bbc76a71430</a>
  - 「This is an apple」をBoWでベクトル化すると[1, 0, 0 ,1, 1, 01, ...]となる。
    - ![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F265344%2F04fea720-330f-2f83-b00b-afb93bcad2d0.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=5841ca0df41da2b1a265ecc43a1cfebd)

## TF-IDF | Term Frequency–Inverse Document Frequency

- 情報検索の分野で、ある文章をベクトルで表現するための手法の一種。
- Bag of Wordsの改良版。
- 語順は考慮されない。
- ある文章$d$の各単語$t$に対して、その単語$t$がどれくらい重要かを表す統計量$\text{tf-idf}(t,d)$を計算し(※下記式参照)、全単語分並べたベクトルを以って、その文章$d$を表すベクトルとする。
  - 第一項$\text{tf}(t,d)$は、Term frequency (単語頻度)、すなわちある文書$d$内でのある単語$t$の出現頻度である。
  - 第二項$\log \frac{N}{\text{df}(t)}$は、Inverse document frequency (逆文書頻度)、すなわちある単語$t$が全文章内でどれだけ珍しいかを示す項で、ある単語$t$を含む文書数を総文章数$N$で除算し、その商の逆数の対数をとったものである。
    - これは、例えば"the"という非常に普遍的で高頻出な単語を多く含む文書を誤って重要視してしまうことを避けるために用いられる。

$$
\text{tf-idf}(t,d) = \text{tf}(t,d) \cdot \log \frac{N}{\text{df}(t)} \\
$$