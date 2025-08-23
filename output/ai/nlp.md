<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md# -->

## 自然言語処理 | NLP | Natural Language Processing<a id="6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">人工知能</a>の研究分野の1つで、人間の言語(=自然言語)を計算機で処理・理解・生成することを目的とする。
- 当初、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>は主に画像処理の分野で発展したが、2010年代後半から<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>の分野でも<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>ベースの手法が導入され、現代の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">大規模言語モデル</a>へ発展した。
- 代表的な応用例:
  - 機械翻訳(例: Google翻訳, DeepLなど)
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6Z+z5aOw6KqN6K2YIHwgQXV0b21hdGljIFNwZWVjaCBSZWNvZ25pdGlvbiB8IEFTUg==">音声認識</a>
  - 質問応答
  - 要約
  - 感情分析
- 歴史的な流れ:

|年代|タイトル|概要|代表例|課題|
|:----|:----|:----|:----|:----|
|1950〜1980年代|ルールベース時代|手書きの文法規則や辞書に基づく処理|ELIZA(初期の対話システム), SYSTRAN(初期の機械翻訳)|言語の曖昧性や多様性に対応しきれない|
|1990年代|統計的手法の時代|大規模<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44Kz44O844OR44K5IHwgQ29ycHVz">コーパス</a>から確率モデルを学習|n-gram(確率的言語モデル),Hidden Markov Model(HMM)による品詞タグ付けや<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6Z+z5aOw6KqN6K2YIHwgQXV0b21hdGljIFNwZWVjaCBSZWNvZ25pdGlvbiB8IEFTUg==">音声認識</a>, <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#VEYtSURGIHwgVGVybSBGcmVxdWVuY3nigJNJbnZlcnNlIERvY3VtZW50IEZyZXF1ZW5jeQ==">TF-IDF</a>, <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#5Y2Y6Kqe6KKL44Oi44OH44OrIHwgQmFnIG9mIFdvcmRzIHwgQm9X">Bag of Words</a> による文書検索・<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5YiG6aGeIHwgQ2xhc3NpZmljYXRpb24=">分類</a>|文脈を短距離（n単語）しか扱えない。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Kqe5b2ZIHwgVm9jYWJ1bGFyeQ==">語彙</a>外(OOV)問題が深刻。|
|2010年代前半|分散表現の時代|単語を高次元の疎ベクトルではなく、低次元の密ベクトル (embedding) で表現|Word2Vec (2013, Mikolovら)により、単語間の意味的類似性（king - man + woman ≈ queen）が捉えられる。|文脈による単語の意味の変化を扱えない。|
|2010年代後半|ニューラル<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">NLP</a>の時代|<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>ベースの手法が導入された|Seq2Seq、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44Oq44Kr44Os44Oz44OI44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgUk5OIHwgUmVjdXJyZW50IE5ldXJhbCBOZXR3b3Jr">RNN</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md#TFNUTSB8IExvbmcgU2hvcnQtVGVybSBNZW1vcnk=">LSTM</a>|長距離依存性に弱い。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6Kqk5beu6YCG5Lyd5pKt5rOVIHwg44OQ44OD44Kv44OX44Ot44OR44Ky44O844K344On44OzIHwgQmFja3Byb3BhZ2F0aW9u">誤差逆伝播法</a>での学習で単語方向にモデルが深くなり、勾配消失もしくは勾配爆発が起きやすい。|
|2020年代～現代|<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">大規模言語モデル</a>の時代|<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデルのパラメータ数が、数十億〜数兆規模に。GPTの導入。|Open<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>社ChatGPT、Google社Gemini/Gemma、Meta社Llama、Anthropic社Claude|-|

## コーパス | Corpus<a id="44Kz44O844OR44K5IHwgQ29ycHVz"></a>

- テキストデータのデータセット。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>の分野で、解析対象となる文書群全体のこと。
- テキストデータの具体例:
  - ウェブページ
  - 記事
  - 論文
  - 特許
  - カルテ
- 具体例:
  - 国立国語研究所の日本語<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44Kz44O844OR44K5IHwgQ29ycHVz">コーパス</a>
    - 話し言葉・会話<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44Kz44O844OR44K5IHwgQ29ycHVz">コーパス</a> <a href="https://pj.ninjal.ac.jp/corpus_center">https://pj.ninjal.ac.jp/corpus_center</a>
    - ウェブ<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44Kz44O844OR44K5IHwgQ29ycHVz">コーパス</a> <a href="https://pj.ninjal.ac.jp/corpus_center/nwjc/">https://pj.ninjal.ac.jp/corpus_center/nwjc/</a>

## トークン | Token<a id="44OI44O844Kv44OzIHwgVG9rZW4="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>とは、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>の処理・モデルが扱う最小単位。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#5b2i5oWL57Sg">形態素</a>と違い、必ずしも意味をもつ最小単位とは限らない。
  - 最新の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>でよく用いられるバイト単位の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OK44Kk44K844O844K344On44OzIHwg44OI44O844Kv44Oz5YiG5YmyIHwgVG9rZW5pemF0aW9u">トークナイゼーション</a>は、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44Kz44O844OR44K5IHwgQ29ycHVz">コーパス</a>内のテキストをバイト単位で解釈し、その出現頻度をもとに<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を形成する。
    - 出現頻度が高いバイト列は、そのバイト列全体を1<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>として扱うが、
    - 逆に出現頻度が少ないバイトはそのバイト単体を1<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>として扱うことになる。
  - 例えば、現代で良く用いられるUTF-8はマルチバイト文字コードであるため、ある出現頻度が低いバイトを表す<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>は、意味はおろか、文字としても意味をなさないことがある。
- 例:
  - (引用元): https://platform.openai.com/tokenizer の「GPT-4o & GPT-4o mini」
  - 東京都の蕎麦
    - ↓
  - 「123558:東京都」+「3385:の」+「14745:�」+「236:�」+ 「100108:麦」
    - 出現頻度の高い「東京都」は3文字をまとめて1つの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>として扱われている
    - 出現頻度の低い「蕎」は1文字をさらにバイト単位に分割され、2つの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>として扱われている

## トークナイゼーション | トークン分割 | Tokenization<a id="44OI44O844Kv44OK44Kk44K844O844K344On44OzIHwg44OI44O844Kv44Oz5YiG5YmyIHwgVG9rZW5pemF0aW9u"></a>

- テキストを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>に分割すること
- 分割の粒度は、手法により様々:
  - 単語単位（Word-level tokenization）
    - 例: "I love <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">NLP</a>" → \["I", "love", "<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">NLP</a>"\]
    - 課題:
  - 文字単位（Character-level tokenization）
    - 例: "cat" → ["c", "a", "t"]
    - 課題: 長系列化(入力テキストが長大な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>の列になり、言語モデルの性能に悪影響)
  - サブワード単位（<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#QlBFIHwgQnl0ZSBQYWlyIEVuY29kaW5n">BPE</a>, <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#U2VudGVuY2VQaWVjZQ==">SentencePiece</a>, WordPiece）
    - 例: "unbelievable" → ["un", "believ", "able"] ※ 頻度が高いサブワードに優先的に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を割り当てる
    - 例: 「東京都の蕎麦」→ 「123558:東京都」+「3385:の」+「14745:�」+「236:�」+ 「100108:麦」※ 頻度が高いバイト列に優先的に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を割り当てる
- 古典的な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>では「単語単位」、最近の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>では「サブワード単位」か「バイト単位」が主流。

## デトークナイゼーション | Detokenization<a id="44OH44OI44O844Kv44OK44Kk44K844O844K344On44OzIHwgRGV0b2tlbml6YXRpb24="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>列を元のテキストに戻す処理
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OK44Kk44K844O844K344On44OzIHwg44OI44O844Kv44Oz5YiG5YmyIHwgVG9rZW5pemF0aW9u">トークナイゼーション</a>の逆の処理
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>等の自然言語を生成するモデルが、出力の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>列を生成し、その<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>列をテキストに変換するのに利用される

## トークナイザ | Tokenizer<a id="44OI44O844Kv44OK44Kk44K2IHwgVG9rZW5pemVy"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OK44Kk44K844O844K344On44OzIHwg44OI44O844Kv44Oz5YiG5YmyIHwgVG9rZW5pemF0aW9u">トークナイゼーション</a>/<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OH44OI44O844Kv44OK44Kk44K844O844K344On44OzIHwgRGV0b2tlbml6YXRpb24=">デトークナイゼーション</a>を行うためのアルゴリズムやツールのこと
- 具体例: ※ 現代の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>で良く用いられる<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OK44Kk44K2IHwgVG9rZW5pemVy">トークナイザ</a>を列挙。全てサブワード分割の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OK44Kk44K844O844K344On44OzIHwg44OI44O844Kv44Oz5YiG5YmyIHwgVG9rZW5pemF0aW9u">トークナイゼーション</a>を行う。
  - WordPiece
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#U2VudGVuY2VQaWVjZQ==">SentencePiece</a>
  - Byte pair encoding
  - tiktoken

## 形態素<a id="5b2i5oWL57Sg"></a>

- 言語学における最小の意味を担う単位
- 例:
  - 「食べました」
    - ↓
  - 「食べ (動詞語幹)」 + 「ま (丁寧接頭)」 + 「し (過去助動詞語幹)」 + 「た (活用語尾)」

## 形態素解析<a id="5b2i5oWL57Sg6Kej5p6Q"></a>

- テキストを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#5b2i5oWL57Sg">形態素</a>に分割すること
  - テキストの構造を解析し、分割し、分割したそれぞれに品詞や語形、活用形などの情報を付与する
- 特に 日本語や中国語のように単語境界が空白で明示されない言語 において必須の前処理。
- 処理の流れ
  1. **分割 (<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OK44Kk44K844O844K344On44OzIHwg44OI44O844Kv44Oz5YiG5YmyIHwgVG9rZW5pemF0aW9u">Tokenization</a>/<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#44K744Kw44Oh44Oz44OG44O844K344On44OzIHwgU2VnbWVudGF0aW9u">Segmentation</a>)**: 文を<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#5b2i5oWL57Sg">形態素</a>単位に切り分ける（<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#5YiG44GL44Gh5pu444GNIHwg5Y2Y6Kqe5YiG5Ymy">分かち書き</a>）。
  1. **品詞付与 (Part-of-Speech Tagging)**: 各<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#5b2i5oWL57Sg">形態素</a>に対して品詞や活用形などの情報をラベル付け。
  1. **<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5q2j6KaP5YyWIHwgUmVndWxhcml6YXRpb24=">正規化</a> (<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5q2j6KaP5YyWIHwgTm9ybWFsaXphdGlvbg==">Normalization</a>)**: 活用形を基本形に変換（例: 「走った」→「走る」）。
- 例:
  - 私は<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>が好きです
    - ↓
  - ※ 下記参照(MeCabの例)

```
私    名詞,代名詞,一般,*,*,*,私,ワタシ,ワタシ
は    助詞,係助詞,*,*,*,*,は,ハ,ワ
自然  名詞,一般,*,*,*,*,自然,シゼン,シゼン
言語  名詞,一般,*,*,*,*,言語,ゲンゴ,ゲンゴ
処理  名詞,サ変接続,*,*,*,*,処理,ショリ,ショリ
が    助詞,格助詞,一般,*,*,*,が,ガ,ガ
好き  名詞,形容動詞語幹,*,*,*,*,好き,スキ,スキ
です  助動詞,*,*,*,特殊・デス,基本形,です,デス,デス
```

- 手法の例:
  - **辞書ベース + 動的計画法**
    - MeCab: IPA辞書やUniDicを利用、Viterbiアルゴリズムで最適な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#5b2i5oWL57Sg">形態素</a>列を探索。
  - **<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5qmf5qKw5a2m57+SIHwgTWFjaGluZSBMZWFybmluZw==">機械学習</a>ベース**
    - CRF (Conditional Random Field)、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#44K144Od44O844OI44OZ44Kv44K/44O844Oe44K344OzIHwgU1ZN">SVM</a> による系列ラベリング。
  - **<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>ベース**
    - Bi<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md#TFNUTSB8IExvbmcgU2hvcnQtVGVybSBNZW1vcnk=">LSTM</a>-CRF, <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a> によるエンドツーエンド<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#5b2i5oWL57Sg6Kej5p6Q">形態素解析</a>器。

## 分かち書き | 単語分割<a id="5YiG44GL44Gh5pu444GNIHwg5Y2Y6Kqe5YiG5Ymy"></a>

- 日本語や中国語のように単語境界を空白で明示しない言語において、テキストとを単語単位に分割すること
  - 英語の場合，テキストをスペースやカンマで区切れば単純な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#5YiG44GL44Gh5pu444GNIHwg5Y2Y6Kqe5YiG5Ymy">分かち書き</a>が可能
- 単語単位の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OK44Kk44K844O844K344On44OzIHwg44OI44O844Kv44Oz5YiG5YmyIHwgVG9rZW5pemF0aW9u">トークナイゼーション</a>に相当

## リカレントニューラルネットワーク | RNN | Recurrent Neural Network<a id="44Oq44Kr44Os44Oz44OI44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgUk5OIHwgUmVjdXJyZW50IE5ldXJhbCBOZXR3b3Jr"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>で良く用いられる<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデルの構造の1種。
- 入力系列を1つずつ逐次的に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>に入力し、中間層の値を内部に保持していて、入力と中間層から出力を計算する。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>。このような構造により、入力系列の時間的依存関係を捉えることができる。
- この特徴が、入力も出力も可変長な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>に適していたため、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>の分野で広く用いられていた。

**<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44Oq44Kr44Os44Oz44OI44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgUk5OIHwgUmVjdXJyZW50IE5ldXJhbCBOZXR3b3Jr">RNN</a>の課題:**

- 原理上は<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>間の長期依存性を捉えることがでるが、固定長ベクトルであるアクティベーションだけでは、長期依存性の情報を保持しきれない
- `ネットワークが単語位置方向に深くなるため、学習が難しい。勾配消失もしくは勾配爆発が起きやすい`
- (引用元): <a href="https://speakerdeck.com/chokkan/20230327_riken_llm?slide=12">https://speakerdeck.com/chokkan/20230327_riken_llm?slide=12</a>
  - ![alt text](./llm.md.RNN_0.png)

## エンべディング | Embedding<a id="44Ko44Oz44G544OH44Kj44Oz44KwIHwgRW1iZWRkaW5n"></a>

- 離散<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を連続値ベクトル空間へ写像する手法。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Kqe5b2ZIHwgVm9jYWJ1bGFyeQ==">語彙</a>空間のワンホットベクトルを低次元密ベクトルに変換し、意味的距離の保存を目指す。
- 通常は入力<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44Ko44Oz44G544OH44Kj44Oz44KwIHwgRW1iZWRkaW5n">エンべディング</a>と位置<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44Ko44Oz44G544OH44Kj44Oz44KwIHwgRW1iZWRkaW5n">エンべディング</a>の加算で初期入力が構成される。

## SentencePiece<a id="U2VudGVuY2VQaWVjZQ=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>化を言語非依存に行うためのサブワード単位<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OK44Kk44K2IHwgVG9rZW5pemVy">トークナイザ</a>ー。Unigram Language Modelまたは<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#QlBFIHwgQnl0ZSBQYWlyIEVuY29kaW5n">BPE</a>に基づき、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Kqe5b2ZIHwgVm9jYWJ1bGFyeQ==">語彙</a>と分割境界を学習する。スペースを専用<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>として扱うことで前処理不要。

## BPE | Byte Pair Encoding<a id="QlBFIHwgQnl0ZSBQYWlyIEVuY29kaW5n"></a>

- 頻出ペアのマージ操作を繰り返して<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Kqe5b2ZIHwgVm9jYWJ1bGFyeQ==">語彙</a>を構成するデータ圧系サブワード分割アルゴリズム。単語の分割可能性を保ちつつ、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Kqe5b2ZIHwgVm9jYWJ1bGFyeQ==">語彙</a>サイズと未出語処理のトレードオフを実現。

## コサイン類似度 | Cosine Similarity<a id="44Kz44K144Kk44Oz6aGe5Ly85bqmIHwgQ29zaW5lIFNpbWlsYXJpdHk="></a>

- ベクトル間の角度のコサイン値で類似度を測定。エンベディング間比較に使用。

## 語彙 | Vocabulary<a id="6Kqe5b2ZIHwgVm9jYWJ1bGFyeQ=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44Kz44O844OR44K5IHwgQ29ycHVz">コーパス</a>内に現れる全ての単語を集めたもの

## 単語袋モデル | Bag of Words | BoW<a id="5Y2Y6Kqe6KKL44Oi44OH44OrIHwgQmFnIG9mIFdvcmRzIHwgQm9X"></a>

- 情報検索の分野で、ある文章をベクトルで表現するための手法の一種。
- ある文章$d$に対して、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Kqe5b2ZIHwgVm9jYWJ1bGFyeQ==">語彙</a>に含まれる単語の出現回数をカウントし、それを以ってその文章$d$を表すベクトルする。
- 語順は考慮されない。
- 具体例:
  - (引用元): <a href="https://qiita.com/kazukiii/items/d717add45bbc76a71430">https://qiita.com/kazukiii/items/d717add45bbc76a71430</a>
  - 「This is an apple」を<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#5Y2Y6Kqe6KKL44Oi44OH44OrIHwgQmFnIG9mIFdvcmRzIHwgQm9X">BoW</a>でベクトル化すると[1, 0, 0 ,1, 1, 01, ...]となる。
    - ![](https://qiita-user-contents.imgix.net/https%3A%2F%2Fqiita-image-store.s3.amazonaws.com%2F0%2F265344%2F04fea720-330f-2f83-b00b-afb93bcad2d0.png?ixlib=rb-4.0.0&auto=format&gif-q=60&q=75&s=5841ca0df41da2b1a265ecc43a1cfebd)

## TF-IDF | Term Frequency–Inverse Document Frequency<a id="VEYtSURGIHwgVGVybSBGcmVxdWVuY3nigJNJbnZlcnNlIERvY3VtZW50IEZyZXF1ZW5jeQ=="></a>

- 情報検索の分野で、ある文章をベクトルで表現するための手法の一種。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#5Y2Y6Kqe6KKL44Oi44OH44OrIHwgQmFnIG9mIFdvcmRzIHwgQm9X">Bag of Words</a>の改良版。
- 語順は考慮されない。
- ある文章$d$の各単語$t$に対して、その単語$t$がどれくらい重要かを表す統計量$\\text{tf-idf}(t,d)$を計算し(※下記式参照)、全単語分並べたベクトルを以って、その文章$d$を表すベクトルとする。
  - 第一項$\\text{tf}(t,d)$は、Term frequency (単語頻度)、すなわちある文書$d$内でのある単語$t$の出現頻度である。
  - 第二項$\\log \\frac{N}{\\text{df}(t)}$は、Inverse document frequency (逆文書頻度)、すなわちある単語$t$が全文章内でどれだけ珍しいかを示す項で、ある単語$t$を含む文書数を総文章数$N$で除算し、その商の逆数の対数をとったものである。
    - これは、例えば"the"という非常に普遍的で高頻出な単語を多く含む文書を誤って重要視してしまうことを避けるために用いられる。

$$
\\text{tf-idf}(t,d) = \\text{tf}(t,d) \\cdot \\log \\frac{N}{\\text{df}(t)} \\
$$

# 参考文献

<!--- 数理・データサイエンス・AI教育強化拠点コンソーシアム https://www.mi.u-tokyo.ac.jp/6university_consortium.html --->

- <a href="https://www.mi.u-tokyo.ac.jp/consortium2/pdf/4-5_literacy_level_note_2024rev.pdf">https://www.mi.u-tokyo.ac.jp/consortium2/pdf/4-5_literacy_level_note_2024rev.pdf</a>
