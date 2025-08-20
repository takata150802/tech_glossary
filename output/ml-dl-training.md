<!-- 記事タイトル:用語解説集-機械学習-深層学習-学習関連 -->

<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-training.md# -->

## 転移学習 | Transfer Learning<a id="6Lui56e75a2m57+SIHwgVHJhbnNmZXIgTGVhcm5pbmc="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-training.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc=">ファインチューニング</a>と同様、ある学習済み<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>モデルをもう一度学習させること。
- ただし、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-training.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc=">ファインチューニング</a>とは違い、新たに学習させるタスクは学習済み<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>モデルのタスクのサブセットと決まっているわけではない。似ているが同一でないタスクである。
- 一般的には、元の学習済み<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>モデルに新たなレイヤーを追加しこの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg==">重み</a>に新しいタスクを学習させる。既存のレイヤーはフリーズさせる。つまり、既存のレイヤーの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5a2m57+S546HIHwgTGVhcm5pbmcgUmF0ZQ==">学習率</a>は0とする。

## ファインチューニング | Fine-tuning<a id="44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-training.md#6Lui56e75a2m57+SIHwgVHJhbnNmZXIgTGVhcm5pbmc=">転移学習</a>と同様、ある学習済み<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>モデルをもう一度学習させること。
- 一般的には、新たに学習させるタスクは学習済み<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>モデルのタスクのサブセットである。
- 一般的には、元の学習済み<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>モデルに新たなレイヤーを追加しこの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg==">重み</a>に新しいタスクを学習させる。既存のレイヤーも学習させるが、既存のレイヤーの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#5a2m57+S546HIHwgTGVhcm5pbmcgUmF0ZQ==">学習率</a>は低めにする。
  る。

## Zero-Shot Learning<a id="WmVyby1TaG90IExlYXJuaW5n"></a>

- 教師データに無いカテゴリを予測する問題設定。

## Few-Shot Learning<a id="RmV3LVNob3QgTGVhcm5pbmc="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-training.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc=">ファインチューニング</a>や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-training.md#6Lui56e75a2m57+SIHwgVHJhbnNmZXIgTGVhcm5pbmc=">転移学習</a>と同様、ある学習済み<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>モデルをもう一度学習させること。
- ただし、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-training.md#44OV44Kh44Kk44Oz44OB44Ol44O844OL44Oz44KwIHwgRmluZS10dW5pbmc=">ファインチューニング</a>や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-training.md#6Lui56e75a2m57+SIHwgVHJhbnNmZXIgTGVhcm5pbmc=">転移学習</a>は大量の教師データを用いるのが一般的であるが、非常に少量の教師データで<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>モデルを学習させようとする問題設定。
