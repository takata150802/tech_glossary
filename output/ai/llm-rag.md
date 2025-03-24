<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-rag.md# -->

## RAG | Retrieval-Augmented Generation<a id="UkFHIHwgUmV0cmlldmFsLUF1Z21lbnRlZCBHZW5lcmF0aW9u"></a>

- 外部の検索モジュールから文書を取得し、そのコンテキストを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OX44Ot44Oz44OX44OIIHwgUHJvbXB0">プロンプト</a>に付加して生成を行う手法。

## リランク | Rerank<a id="44Oq44Op44Oz44KvIHwgUmVyYW5r"></a>

- 初期レトリーバブルな候補（例：BM25やDPRで抽出）に対し、クロスエンコーダやランキングモデルを用いて文脈整合性や関連度に基づいて再スコアリング・再順位付けを行うプロセ。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-rag.md#UkFHIHwgUmV0cmlldmFsLUF1Z21lbnRlZCBHZW5lcmF0aW9u">RAG</a>におけるretriever-refiner構成で用いられる。
