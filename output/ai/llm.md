<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md# -->

## 大規模言語モデル| Large Language Model | LLM<a id="5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md#VHJhbnNmb3JtZXI=">Transformer</a>ベースのアーキテクチャを用いて、大規模なコーパスを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6Ieq5bex5pWZ5bir44GC44KK5a2m57+SIHwgU2VsZi1zdXBlcnZpc2VkIExlYXJuaW5n">自己教師あり学習</a>により<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJldHJhaW5pbmc=">事前学習</a>した自然言語生成モデル。

## 推論 | Inference<a id="5o6o6KuWIHwgSW5mZXJlbmNl"></a>

- 学習済みモデルに対して<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OX44Ot44Oz44OX44OIIHwgUHJvbXB0">プロンプト</a>を与え、次の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>またはテキスト全体を生成させる処理。

## プロンプト | Prompt<a id="44OX44Ot44Oz44OX44OIIHwgUHJvbXB0"></a>

- モデルへの入力文。コンテキストや命令、質問などを含むことが多く、Zero-shotやFew-shotにも活用される。

## デコーダー | Decoder<a id="44OH44Kz44O844OA44O8IHwgRGVjb2Rlcg=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md#VHJhbnNmb3JtZXI=">Transformer</a>における出力生成側のネットワーク構造で、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#6Ieq5bex5Zue5biwIHwgQXV0b3JlZ3Jlc3NpdmU=">自己回帰</a>的に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を予測する。

## RMSNorm | LayerNorm<a id="Uk1TTm9ybSB8IExheWVyTm9ybQ=="></a>

- 各レイヤーにおいて出力のスケーリングを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5q2j6KaP5YyWIHwgUmVndWxhcml6YXRpb24=">正規化</a>し勾配の安定性を高めるテクニック。

## 位置エンコーディング | Positional Encoding<a id="5L2N572u44Ko44Oz44Kz44O844OH44Kj44Oz44KwIHwgUG9zaXRpb25hbCBFbmNvZGluZw=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>の系列順序情報をモデルに与えるための埋め込み。絶対位置または相対位置を採用。

## アテンション | Attention<a id="44Ki44OG44Oz44K344On44OzIHwgQXR0ZW50aW9u"></a>

- 各<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>が他の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>との関連性を計算するメカニズム。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#U2VsZi1BdHRlbnRpb24=">Self-Attention</a>が<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md#VHJhbnNmb3JtZXI=">Transformer</a>の要。

## 自己回帰 | Autoregressive<a id="6Ieq5bex5Zue5biwIHwgQXV0b3JlZ3Jlc3NpdmU="></a>

- 入力の過去の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を使って次の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を逐次生成するモデル構造。GPT系列などが該当。

## コンテキスト長 | Context Length | Context Window<a id="44Kz44Oz44OG44Kt44K544OI6ZW3IHwgQ29udGV4dCBMZW5ndGggfCBDb250ZXh0IFdpbmRvdw=="></a>

- モデルが一度に処理可能な最大<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>数。大きいほど長文処理能力が向上するが、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwgQXR0ZW50aW9u">アテンション</a>の計算量が増大する。

## FlashAttention<a id="Rmxhc2hBdHRlbnRpb24="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwgQXR0ZW50aW9u">アテンション</a>計算をメモリアクセス最適化により高速化したアルゴリズム。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md#VHJhbnNmb3JtZXI=">Transformer</a>のスケーラビリティを改善。

## Mixture of Experts | MoE<a id="TWl4dHVyZSBvZiBFeHBlcnRzIHwgTW9F"></a>

- 複数のサブネットワーク（専門家）を用意し、入力ごとに一部のみを動かすことで、計算量を抑えつつモデルの能力を拡張。

## Sparse Transformer<a id="U3BhcnNlIFRyYW5zZm9ybWVy"></a>

- 全<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>間の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwgQXR0ZW50aW9u">アテンション</a>ではなく、一部の接続のみ有効にすることで、計算量とメモリ使用を削減した<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md#VHJhbnNmb3JtZXI=">Transformer</a>の変種。

## トークン | Token<a id="44OI44O844Kv44OzIHwgVG9rZW4="></a>

- モデルの入出力単位であり、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#QlBFIHwgQnl0ZSBQYWlyIEVuY29kaW5n">BPE</a>や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#U2VudGVuY2VQaWVjZQ==">SentencePiece</a>などのサブワード分割により生成される。

## トークナイザー | トークナイザ | Tokenizer<a id="44OI44O844Kv44OK44Kk44K244O8IHwg44OI44O844Kv44OK44Kk44K2IHwgVG9rZW5pemVy"></a>

- 生テキストをサブワード単位の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>列に変換する処理器で、エンコーディングとデコーディングを担う。

## エンべディング | Embedding<a id="44Ko44Oz44G544OH44Kj44Oz44KwIHwgRW1iZWRkaW5n"></a>

- 離散<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を連続値ベクトル空間へ写像する手法。語彙空間のワンホットベクトルを低次元密ベクトルに変換し、意味的距離の保存を目指す。
- 通常は入力<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ko44Oz44G544OH44Kj44Oz44KwIHwgRW1iZWRkaW5n">エンべディング</a>と位置<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ko44Oz44G544OH44Kj44Oz44KwIHwgRW1iZWRkaW5n">エンべディング</a>の加算で初期入力が構成される。

## Self-Attention<a id="U2VsZi1BdHRlbnRpb24="></a>

- 入力系列内の全<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>ペアに対し、クエリ（Q）、キー（K）、バリュー（V）の内積スコアをSoftmax<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5q2j6KaP5YyWIHwgUmVndWxhcml6YXRpb24=">正規化</a>して加重和を取る<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwgQXR0ZW50aW9u">アテンション</a>機構。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-nlp.md#VHJhbnNmb3JtZXI=">Transformer</a>の基盤であり、長距離依存関係の獲得に寄与する。

## SentencePiece<a id="U2VudGVuY2VQaWVjZQ=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>化を言語非依存に行うためのサブワード単位<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OK44Kk44K244O8IHwg44OI44O844Kv44OK44Kk44K2IHwgVG9rZW5pemVy">トークナイザー</a>。Unigram Language Modelまたは<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#QlBFIHwgQnl0ZSBQYWlyIEVuY29kaW5n">BPE</a>に基づき、語彙と分割境界を学習する。スペースを専用<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>として扱うことで前処理不要。

## BPE | Byte Pair Encoding<a id="QlBFIHwgQnl0ZSBQYWlyIEVuY29kaW5n"></a>

- 頻出ペアのマージ操作を繰り返して語彙を構成するデータ圧系サブワード分割アルゴリズム。単語の分割可能性を保ちつつ、語彙サイズと未出語処理のトレードオフを実現。

## コサイン類似度 | Cosine Similarity<a id="44Kz44K144Kk44Oz6aGe5Ly85bqmIHwgQ29zaW5lIFNpbWlsYXJpdHk="></a>

- ベクトル間の角度のコサイン値で類似度を測定。エンベディング間比較に使用。
