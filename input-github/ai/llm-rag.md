<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-rag.md# -->

## RAG | Retrieval-Augmented Generation
- 外部の検索モジュールから文書を取得し、そのコンテキストをプロンプトに付加して生成を行う手法。

## リランク | Rerank
- 初期レトリーバブルな候補（例：BM25やDPRで抽出）に対し、クロスエンコーダやランキングモデルを用いて文脈整合性や関連度に基づいて再スコアリング・再順位付けを行うプロセ。
- RAGにおけるretriever-refiner構成で用いられる。

