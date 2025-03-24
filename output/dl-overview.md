<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md# -->

## 深層学習 | Deep Learning<a id="5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw=="></a>

- 複数の層を持つ<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>を使用してデータから特徴を自動的に学習する<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5qmf5qKw5a2m57+SIHwgTWFjaGluZSBMZWFybmluZw==">機械学習</a>の一分野です。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">Deep Learning</a> is a subfield of machine learning that uses neural networks with multiple layers to automatically learn features from data.

## ニューラルネットワーク | Neural Network<a id="44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms="></a>

- 単純パーセプトロン,ロジスティック<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5Zue5biwIHwgUmVncmVzc2lvbg==">回帰</a>を多層にしたもの。
  - 多層にすることで線形分離可能でない問題を解くことができるようになった。
  - 課題は<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>の学習の手法であったが、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#6Kqk5beu6YCG5Lyd5pKt5rOVIHwg44OQ44OD44Kv44OX44Ot44OR44Ky44O844K344On44OzIHwgQmFja3Byb3BhZ2F0aW9u">誤差逆伝播法</a>が提唱され(1986年)、2010年代の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">Deep Learning</a>で広く用いられることとなった。
- シグモイド関数の代わりに別の非線形関数を用いることも多く、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5rS75oCn5YyW6Zai5pWwIHwgQWN0aXZhdGlvbiBGdW5jdGlvbg==">活性化関数</a>と呼ばれる。

## 畳み込みニューラルネットワーク | Convolutional Neural Network | CNN<a id="55Wz44G/6L6844G/44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgQ29udm9sdXRpb25hbCBOZXVyYWwgTmV0d29yayB8IENOTg=="></a>

- 画像処理に特化した<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>であり、空間的な特徴を捉えるために畳み込み層を使用します。

## リカレントニューラルネットワーク | Recurrent Neural Network | RNN<a id="44Oq44Kr44Os44Oz44OI44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgUmVjdXJyZW50IE5ldXJhbCBOZXR3b3JrIHwgUk5O"></a>

- 時系列データやシーケンスデータを処理するために、出力を次の入力としてフィードバックする構造を持つ<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgTmV1cmFsIE5ldHdvcms=">ニューラルネットワーク</a>です。

## Long Short-Term Memory | LSTM<a id="TG9uZyBTaG9ydC1UZXJtIE1lbW9yeSB8IExTVE0="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44Oq44Kr44Os44Oz44OI44OL44Ol44O844Op44Or44ON44OD44OI44Ov44O844KvIHwgUmVjdXJyZW50IE5ldXJhbCBOZXR3b3JrIHwgUk5O">リカレントニューラルネットワーク</a>の一種であり、長期間の依存関係を持つデータを効率的に学習することができます。

## 敵対的生成ネットワーク | Generative Adversarial Network | GAN<a id="5pW15a++55qE55Sf5oiQ44ON44OD44OI44Ov44O844KvIHwgR2VuZXJhdGl2ZSBBZHZlcnNhcmlhbCBOZXR3b3JrIHwgR0FO"></a>

- 生成モデルと識別モデルが競い合うことで高品質なデータを生成するモデルです。

## Deepfake<a id="RGVlcGZha2U="></a>

## Seq2Seq Model | Sequence-to-Sequence Model<a id="U2VxMlNlcSBNb2RlbCB8IFNlcXVlbmNlLXRvLVNlcXVlbmNlIE1vZGVs"></a>

## 変分オートエンコーダー | Variational Autoencoder | VAE<a id="5aSJ5YiG44Kq44O844OI44Ko44Oz44Kz44O844OA44O8IHwgVmFyaWF0aW9uYWwgQXV0b2VuY29kZXIgfCBWQUU="></a>

- データの潜在変数を学習し、新しいデータの生成や再構成を行う生成モデルの一種です。

## 転移学習 | Transfer Learning<a id="6Lui56e75a2m57+SIHwgVHJhbnNmZXIgTGVhcm5pbmc="></a>

## fine-Tuning<a id="ZmluZS1UdW5pbmc="></a>

## Q-Learning<a id="US1MZWFybmluZw=="></a>

- エージェントが環境からの報酬に基づいて最適な行動を学習する<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5by35YyW5a2m57+SIHwgUmVpbmZvcmNlbWVudCBMZWFybmluZw==">強化学習</a>アルゴリズムです。

## アテンション機構 | Attention Mechanism<a id="44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIE1lY2hhbmlzbQ=="></a>

## トランスフォーマー | Transformer<a id="44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIE1lY2hhbmlzbQ==">アテンション機構</a>を用いて<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5nIHwgTkxQ">自然言語処理</a>において高い性能を発揮するモデルです。

## Deep Q-Network | DQN<a id="RGVlcCBRLU5ldHdvcmsgfCBEUU4="></a>

- ディープラーニングを用いた<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-overview.md#US1MZWFybmluZw==">Q-Learning</a>の実装であり、エージェントが複雑な環境で最適な行動を学習するために使用されます。

## One-shot Learning<a id="T25lLXNob3QgTGVhcm5pbmc="></a>

- 少ないサンプルで学習を行うことができる技術です。

## Zero-shot Learning<a id="WmVyby1zaG90IExlYXJuaW5n"></a>

- 学習に使用していないクラスを識別することができる技術です。

## プロンプトエンジニアリング | Prompt Engineering<a id="44OX44Ot44Oz44OX44OI44Ko44Oz44K444OL44Ki44Oq44Oz44KwIHwgUHJvbXB0IEVuZ2luZWVyaW5n"></a>

- 生成モデルに対する入力（<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OX44Ot44Oz44OX44OIIHwgUHJvbXB0">プロンプト</a>）を最適化して望ましい出力を得る技術です。

## EMアルゴリズム | Expectation-Maximization Algorithm | EM Algorithm<a id="RU3jgqLjg6vjgrTjg6rjgrrjg6AgfCBFeHBlY3RhdGlvbi1NYXhpbWl6YXRpb24gQWxnb3JpdGhtIHwgRU0gQWxnb3JpdGht"></a>

## 拡散モデル | Diffusion Model<a id="5ouh5pWj44Oi44OH44OrIHwgRGlmZnVzaW9uIE1vZGVs"></a>
