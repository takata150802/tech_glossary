<!-- 記事タイトル:用語解説集-機械学習-深層学習-言語系 -->

<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md# -->

## Transformer<a id="VHJhbnNmb3JtZXI="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5nIHwgTkxQ">自然言語処理</a>タスクにおける革新的なモデルアーキテクチャであり、従来の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44Oq44Kr44Os44Oz44OI44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgUmVjdXJyZW50IE5ldXJhbCBOZXR3b3JrIHwgUk5O">リカレントニューラルネットワーク</a>（<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44Oq44Kr44Os44Oz44OI44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgUmVjdXJyZW50IE5ldXJhbCBOZXR3b3JrIHwgUk5O">RNN</a>）や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#55Wz44G/6L6844G/44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgQ29udm9sdXRpb25hbCBOZXVyYWwgTmV0d29yayB8IENOTg==">畳み込みニューラルネットワーク</a>（<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#55Wz44G/6L6844G/44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgQ29udm9sdXRpb25hbCBOZXVyYWwgTmV0d29yayB8IENOTg==">CNN</a>）に代わるものとして注目された。
- シーケンスからシーケンスへの変換（例: 機械翻訳）、文章の生成、質問応答などのさまざまな<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5nIHwgTkxQ">自然言語処理</a>タスクで成功を収めました。

## Attention Is All You Need<a id="QXR0ZW50aW9uIElzIEFsbCBZb3UgTmVlZA=="></a>

- 2017年にGoogleの研究者によって提案された論文。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md#VHJhbnNmb3JtZXI=">Transformer</a>と呼ばれる<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>アーキテクチャを導入した。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/llm-overview.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrIHwgTGFyZ2UgTGFuZ3VhZ2UgTW9kZWwgfCBMTE0=">LLM</a>

## LSTM | Long Short-Term Memory<a id="TFNUTSB8IExvbmcgU2hvcnQtVGVybSBNZW1vcnk="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44Oq44Kr44Os44Oz44OI44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgUmVjdXJyZW50IE5ldXJhbCBOZXR3b3JrIHwgUk5O">リカレントニューラルネットワーク</a>（<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44Oq44Kr44Os44Oz44OI44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgUmVjdXJyZW50IE5ldXJhbCBOZXR3b3JrIHwgUk5O">RNN</a>）の一種。
- 長期的な依存関係を学習するのに適したアーキテクチャ。
- 通常、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5nIHwgTkxQ">自然言語処理</a>や時系列データなどのシーケンスデータのモデリングに使用される。

## トークン化 | Tokenization<a id="44OI44O844Kv44Oz5YyWIHwgVG9rZW5pemF0aW9u"></a>

- ある文章を、単語、句読点、数字、記号などに分割すること。
- 文章を数理モデルで扱える形式に変換するために行う。

## Embedding<a id="RW1iZWRkaW5n"></a>

- トークン(<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md#44OI44O844Kv44Oz5YyWIHwgVG9rZW5pemF0aW9u">トークン化</a>参照)を実数のベクトルに変換すること。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md#44OI44O844Kv44Oz5YyWIHwgVG9rZW5pemF0aW9u">トークン化</a>と同様、文章を数理モデルで扱える形式に変換するために行う。
