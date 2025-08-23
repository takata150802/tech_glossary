<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md# -->

## 自然言語処理 | NLP
- 言語的構造を持つ非構造データを扱う機械学習分野。トークン化、エンベディング、Attention機構を含む。

## リカレントニューラルネットワーク | RNN | Recurrent Neural Network
- 自然言語処理で良く用いられる深層学習モデルの構造の1種。
- 入力系列を1つずつ逐次的にニューラルネットワークに入力し、中間層の値を内部に保持していて、入力と中間層から出力を計算する。ニューラルネットワーク。このような構造により、入力系列の時間的依存関係を捉えることができる。
- この特徴が、入力も出力も可変長な自然言語処理に適していたため、自然言語処理の分野で広く用いられていた。

**RNNの課題:**
- `原理上はトークン間の長期依存性を捉えることがでるが、固定長ベクトルであるアクティベーションだけでは、長期依存性の情報を保持しきれない`
- `ネットワークが単語位置方向に深くなるため、学習が難しい。勾配消失もしくは勾配爆発が起きやすい`
- (引用元): <a href="https://speakerdeck.com/chokkan/20230327_riken_llm?slide=12">https://speakerdeck.com/chokkan/20230327_riken_llm?slide=12</a>
  - ![alt text](./llm.md.RNN_0.png)

## トークン | Token
- モデルの入出力単位であり、BPEやSentencePieceなどのサブワード分割により生成される。

## トークナイザー | トークナイザ | Tokenizer
- 生テキストをサブワード単位のトークン列に変換する処理器で、エンコーディングとデコーディングを担う。

## エンべディング | Embedding
- 離散トークンを連続値ベクトル空間へ写像する手法。語彙空間のワンホットベクトルを低次元密ベクトルに変換し、意味的距離の保存を目指す。
- 通常は入力エンべディングと位置エンべディングの加算で初期入力が構成される。

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
