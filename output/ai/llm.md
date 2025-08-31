<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md# -->

## 大規模言語モデル| Large Language Model | LLM<a id="5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ=="></a>

- 大規模な計算資源を使い、一般的に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>ベースの大規模な言語モデルを、Web上から収集した大規模なテキストデータで学習させたモデル。
  - 2010年代、**主に画像認識や<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#54mp5L2T5qSc5Ye6IHwgT2JqZWN0IERldGVjdGlvbg==">物体検出</a>を行う画像系の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデルの研究開発が注目を集め、本来ゲーミング用途に使われるGPUが<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデルの研究開発に用いられるようになった(GPGPUの一環)**。その後、Google社主導の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#VGVuc29yRmxvdw==">TensorFlow</a>やMeta社(旧Facebook社)主導の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#UHlUb3JjaA==">PyTorch</a>といった<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>フレームワークがOSSでライセンスの範囲内で自由に利用できることも手伝って、**大規模なGPU計算資源を使った<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデルの学習が様々な研究機関・大学・企業で行われるようになった。**
  - 2017年、**Google社の論文「<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwg44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIHwgQXR0ZW50aW9uIG1lY2hhbmlzbQ==">Attention</a> Is All You Need」にて提唱された自然言語系の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデル<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>は、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>、特に機械翻訳の分野で優れた性能を示し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>のおける<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>のブレイクスルー**となった。この<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデル<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>の最も重要なアイディアである<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwg44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIHwgQXR0ZW50aW9uIG1lY2hhbmlzbQ==">アテンション機構</a>は、ほぼ全ての著名な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>が継承しているアイディアであるので、本論文は<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>分野における基礎的な論文とみなされている。
  - 2018年、Open<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>社の論文「Improving Language Understanding by Generative Pre-Training」で初めて、GPT(=いわゆる<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n">事前学習</a>)が提唱された。従来、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>系の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデルは人手でラベル付けしたデータセットで<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5pWZ5bir44GC44KK5a2m57+SIHwgU3VwZXJ2aXNlZCBMZWFybmluZw==">教師あり学習</a>しており、人手でのラベル付けは高コストなため大規模なデータセット構築の制約となっていた。一方で、**GPT(=いわゆる<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-training.md#5LqL5YmN5a2m57+SIHwgUHJlLXRyYWluaW5n">事前学習</a>)は<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5pWZ5bir44Gq44GX5a2m57+SIHwgVW5zdXBlcnZpc2VkIExlYXJuaW5n">教師なし学習</a>のためWeb上から収集した膨大なテキストデータを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデルに学習させることを実現し、大きなブレイクスルー**となった。2022年、Open<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>社がChatGPT(=<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>を用いたChatBotのWebサービス)がリリースされると世間の注目を集め、広く認知されるに至った。2025年現在、北米/中国IT大手が研究開発を牽引し、多くのプロダクト・サービスに<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>が投入され商業的成功を収めている。

**著名な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>:**

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の研究開発競争は激しく、著名な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>は日々アップデートが必要なため下記のサーベイ論文、もしくは<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Oq44O844OA44O844Oc44O844OJIHwgTExN44Oq44O844OA44O844Oc44O844OJIHwgTGVhZGVyYm9hcmQgfCBMTE0gTGVhZGVyYm9hcmQ=">リーダーボード</a>を参照。
  - サーベイ論文:
    - Zhao, Wayne Xin, et al. "A survey of large language models." arXiv preprint arXiv:2303.18223 1.2 (2023).　https://arxiv.org/abs/2303.18223
      - 初版version1は2023年3月31日だが、v2,v3...とアップデートされており、version16が2025年3月11日に公開。
      - ※ 下記図は、本サーベイ論文のFigure.3を引用したものです。
        - ![](./llm.md-ASurveyOfLLM_figure3.png)

## リーダーボード | LLMリーダーボード | Leaderboard | LLM Leaderboard<a id="44Oq44O844OA44O844Oc44O844OJIHwgTExN44Oq44O844OA44O844Oc44O844OJIHwgTGVhZGVyYm9hcmQgfCBMTE0gTGVhZGVyYm9hcmQ="></a>

- 主に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>や画像生成<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5Lq65bel55+l6IO9IHwgQXJ0aWZpY2lhbCBJbnRlbGxpZ2VuY2UgfCBBSQ==">AI</a>の分野で、様々なモデルの性能を客観的に比較・評価するオンラインプラットフォーム
- 具体例:
  - Chatbot Arena:
    - <a href="https://lmarena.ai/leaderboard">https://lmarena.ai/leaderboard</a>
    - LMArenaによる<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Oq44O844OA44O844Oc44O844OJIHwgTExN44Oq44O844OA44O844Oc44O844OJIHwgTGVhZGVyYm9hcmQgfCBMTE0gTGVhZGVyYm9hcmQ=">リーダーボード</a>。
    - **ユーザー投票**でランキングを決める(定量評価も大事だが、ユーザーがどう感じたか?が最も重要というスタンス)。
    - 著名な公開モデルだけでなく、GPT-4oなど**クローズドな商用モデル**もランキングに含まれている。
  - Open <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Oq44O844OA44O844Oc44O844OJIHwgTExN44Oq44O844OA44O844Oc44O844OJIHwgTGVhZGVyYm9hcmQgfCBMTE0gTGVhZGVyYm9hcmQ=">LLM Leaderboard</a>:
    - <a href="https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard">https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard</a>
    - **<a href="https://github.com/takata150802/tech_glossary/blob/main/output/llm-overview.md#SHVnZ2luZyBGYWNl">Hugging Face</a>社による**主に公開モデルの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Oq44O844OA44O844Oc44O844OJIHwgTExN44Oq44O844OA44O844Oc44O844OJIHwgTGVhZGVyYm9hcmQgfCBMTE0gTGVhZGVyYm9hcmQ=">リーダーボード</a>
  - Swallow <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Oq44O844OA44O844Oc44O844OJIHwgTExN44Oq44O844OA44O844Oc44O844OJIHwgTGVhZGVyYm9hcmQgfCBMTE0gTGVhZGVyYm9hcmQ=">LLM Leaderboard</a> v2
    - <a href="https://swallow-llm.github.io/evaluation/index.ja.html">https://swallow-llm.github.io/evaluation/index.ja.html</a>
    - 東京科学大学(旧:東工大)岡崎研・横田研 Swallowプロジェクトが、日本語に強い<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の開発と並行して、公開されている<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の評価実験を独自に進めているもの。**日本語の**評価タスク定量評価が含まれている。
  - Nejumi <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Oq44O844OA44O844Oc44O844OJIHwgTExN44Oq44O844OA44O844Oc44O844OJIHwgTGVhZGVyYm9hcmQgfCBMTE0gTGVhZGVyYm9hcmQ=">LLMリーダーボード</a>3
    - <a href="https://wandb.ai/wandb-japan/llm-leaderboard3/reports/Nejumi-LLM-3--Vmlldzo3OTg2NjM2">https://wandb.ai/wandb-japan/llm-leaderboard3/reports/Nejumi-LLM-3--Vmlldzo3OTg2NjM2</a>
    - WandB社による<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Oq44O844OA44O844Oc44O844OJIHwgTExN44Oq44O844OA44O844Oc44O844OJIHwgTGVhZGVyYm9hcmQgfCBMTE0gTGVhZGVyYm9hcmQ=">リーダーボード</a>。**日本語の**評価タスク定量評価が含まれている。
    - 著名な公開モデルだけでなく、GPT-4oなど**クローズドな商用モデル**もランキングに含まれている。
  - Open Japanese <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Oq44O844OA44O844Oc44O844OJIHwgTExN44Oq44O844OA44O844Oc44O844OJIHwgTGVhZGVyYm9hcmQgfCBMTE0gTGVhZGVyYm9hcmQ=">LLM Leaderboard</a>
    - <a href="https://huggingface.co/spaces/llm-jp/open-japanese-llm-leaderboard">https://huggingface.co/spaces/llm-jp/open-japanese-llm-leaderboard</a>
    - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>-jp による<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Oq44O844OA44O844Oc44O844OJIHwgTExN44Oq44O844OA44O844Oc44O844OJIHwgTGVhZGVyYm9hcmQgfCBMTE0gTGVhZGVyYm9hcmQ=">リーダーボード</a>。 評価ツール llm-jp-eval を活用し、16種類のタスクで日本語の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">大規模言語モデル</a>を評価している。

## Attention is all you need<a id="QXR0ZW50aW9uIGlzIGFsbCB5b3UgbmVlZA=="></a>

- Vaswani, Ashish, et al. "<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#QXR0ZW50aW9uIGlzIGFsbCB5b3UgbmVlZA==">Attention is all you need</a>." Advances in neural information processing systems 30 (2017). https://arxiv.org/abs/1706.03762
- 2017年、Google社の論文
- 本論文にて提唱された自然言語系の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデル<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>は、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>、特に機械翻訳の分野で優れた性能を示し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>のおける<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>のブレイクスルーとなった
- この<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデル<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>の最も重要なアイディアである<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwg44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIHwgQXR0ZW50aW9uIG1lY2hhbmlzbQ==">アテンション機構</a>は、ほぼ全ての著名な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>が継承しているアイディアであるので、本論文は<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>分野における基礎的な論文とみなされている。

## トランスフォーマー | Transformer<a id="44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI="></a>

- 2017年、Google社の論文「<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#QXR0ZW50aW9uIGlzIGFsbCB5b3UgbmVlZA==">Attention is all you need</a>」にて提唱された自然言語系の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデル

  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>、特に機械翻訳の分野で優れた性能を示し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>のおける<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>のブレイクスルーとなった
  - 本モデルの最も重要なアイディアである<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwg44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIHwgQXR0ZW50aW9uIG1lY2hhbmlzbQ==">アテンション機構</a>は、ほぼ全ての著名な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>が継承している

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/llm-overview.md#SHVnZ2luZyBGYWNl">Hugging Face</a>社によるOSSの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>ライブラリの1つ。

  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>に限らず、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#44Kz44Oz44OU44Ol44O844K/44OT44K444On44OzIHwgQ29tcHV0ZXIgVmlzaW9uIHwgQ1Y=">コンピュータビジョン</a>、音声処理、マルチモーダルタスクの最先端のモデルの定義、学習、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>に用いられる
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#UHlUb3JjaA==">PyTorch</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/dl-train_eval.md#VGVuc29yRmxvdw==">TensorFlow</a>、JAXといった主要<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>フレームワークに対応している

## アテンション | アテンション機構 | Attention | Attention mechanism<a id="44Ki44OG44Oz44K344On44OzIHwg44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIHwgQXR0ZW50aW9uIG1lY2hhbmlzbQ=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>で良く用いられる<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデルの構造の1種。

- 著名な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#6Ieq54S26KiA6Kqe5Yem55CGIHwgTkxQIHwgTmF0dXJhbCBMYW5ndWFnZSBQcm9jZXNzaW5n">自然言語処理</a>系の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#5rex5bGk5a2m57+SIHwgRGVlcCBMZWFybmluZw==">深層学習</a>モデル<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>の最も重要なアイディアで、ほぼ全ての著名な<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>が継承しているアイディアである

- (引用元): <a href="https://speakerdeck.com/chokkan/20230327_riken_llm?slide=14">https://speakerdeck.com/chokkan/20230327_riken_llm?slide=14</a>

  - ![alt text](./llm.md.Transformer_0.png)

## パープレキシティ | Perplexity | 困惑度<a id="44OR44O844OX44Os44Kt44K344OG44KjIHwgUGVycGxleGl0eSB8IOWbsOaDkeW6pg=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">大規模言語モデル</a>の分野では、**予測精度の指標の1つ**を指し、最もメジャーな指標。
  - ただし **人間との対話品質**や**事実性**を完全には評価できないため、最近は **MT-Bench, AlpacaEval, Chatbot Arena** などの人間評価指標と併用される。
- **ある入力文に対する正解の出力文を**どれだけ「**困惑せずに**」**予測できるか**を示す。
- 直感的には、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">大規模言語モデル</a>が**次の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を予測するときに**「**平均して何通りの選択肢に迷っているか**」を表す。
  - 厳密には、**次の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>の予測に平均してどれくらいのエントロピー/不確かさがあるか**?を表す。
- **1以上無限大の値を取り、低いほど予測精度が高い良いモデル**。
- 下記数式で定義される。**交差エントロピー誤差のexponentialを取ったものに**等しい。
  - つまり、交差エントロピー誤差は<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の学習の目的関数と良く用いられ、**学習処理中は学習の進捗状況を表す指標**として、**学習処理後はモデルの良し悪しを表す指標**として用いられるのだが、**<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OR44O844OX44Os44Kt44K344OG44KjIHwgUGVycGxleGl0eSB8IOWbsOaDkeW6pg==">パープレキシティ</a>とは単にそのexponentialを取ったものに過ぎない**。

$$
\\text{PPL}(x\_{1:T}) = \\exp\\left(-\\frac{1}{T}\\sum\_{t=1}^T \\log p\_\\theta(x_t \\mid x\_{\\lt t})\\right)
$$

- $T$: シーケンス長
- $p\_\\theta(x_t \\mid x\_{\<t})$: モデルが次<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a> $x_t$ を予測する確率

## 推論 | Inference<a id="5o6o6KuWIHwgSW5mZXJlbmNl"></a>

- 学習済みモデルを使って、新しい入力に対して出力を生成する処理。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">大規模言語モデル</a>の分野では、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OX44Ot44Oz44OX44OIIHwgUHJvbXB0">プロンプト</a>を入力に、以下のいずれかを行うことを指す:
  1. 次の1<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を生成する。
  1. 出力された<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を入力<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OX44Ot44Oz44OX44OIIHwgUHJvbXB0">プロンプト</a>の末尾に加え、再度次の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を生成し、<EOS>が出力されるまで繰り返すテキスト生成。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">大規模言語モデル</a>の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>の設定パラメータ:
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#VGVtcGVyYXR1cmUgfCDmuKnluqbjg5Hjg6njg6Hjg7zjgr8gfCDmuKnluqY=">温度</a> | <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#VGVtcGVyYXR1cmUgfCDmuKnluqbjg5Hjg6njg6Hjg7zjgr8gfCDmuKnluqY=">Temperature</a>
  - Top-k / Top-p
  - Max tokens

## プロンプト | Prompt<a id="44OX44Ot44Oz44OX44OIIHwgUHJvbXB0"></a>

- モデルに与える入力テキスト。タスク指示、質問、文脈、例などを含む。

## デコーダー | Decoder<a id="44OH44Kz44O844OA44O8IHwgRGVjb2Rlcg=="></a>

- シーケンス生成モデルにおける出力系列を逐次生成するモジュール。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>ベースの<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>は、**Encoder-<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OH44Kz44O844OA44O8IHwgRGVjb2Rlcg==">Decoder</a>型**（例: <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-dl-llm.md#VDUgfCBUZXh0LVRvLVRleHQgVHJhbnNmZXIgVHJhbnNmb3JtZXI=">T5</a>）と **<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OH44Kz44O844OA44O8IHwgRGVjb2Rlcg==">Decoder</a>-only型**（例: GPT）に分かれる。

## RMSNorm | Root Mean Square Normalization<a id="Uk1TTm9ybSB8IFJvb3QgTWVhbiBTcXVhcmUgTm9ybWFsaXphdGlvbg=="></a>

- Llama系列の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>でも採用されている<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5q2j6KaP5YyWIHwgUmVndWxhcml6YXRpb24=">正規化</a>層の1つ。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#QXR0ZW50aW9uIGlzIGFsbCB5b3UgbmVlZA==">Attention is all you need</a>の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>で使われていたLayer <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ml-overview.md#5q2j6KaP5YyWIHwgTm9ybWFsaXphdGlvbg==">Normalization</a>の改良。
  - 分散ではなく二乗平均平方根 (RMS) のみで<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5q2j6KaP5YyWIHwgUmVndWxhcml6YXRpb24=">正規化</a>。
  - xの平均を求める必要がない分、計算量が少ない。

$$
\\text{<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#Uk1TTm9ybSB8IFJvb3QgTWVhbiBTcXVhcmUgTm9ybWFsaXphdGlvbg==">RMSNorm</a>}(x) = \\frac{x}{\\text{RMS}(x)} \\cdot g,
\\text{where} \\text{RMS}(x) = \\sqrt{\\frac{1}{d}\\sum\_{i=1}^d x_i^2 + \\epsilon}
$$

- $d$: 次元数
- $g$: 学習可能スケーリング係数

* (引用元): <a href="https://docs.pytorch.org/docs/stable/generated/torch.nn.modules.normalization.RMSNorm.html">https://docs.pytorch.org/docs/stable/generated/torch.nn.modules.normalization.RMSNorm.html</a>

## コンテキスト長 | Context Length | Context Window<a id="44Kz44Oz44OG44Kt44K544OI6ZW3IHwgQ29udGV4dCBMZW5ndGggfCBDb250ZXh0IFdpbmRvdw=="></a>

- モデルが一度に処理できる**入力<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>列の最大長**。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>の計算量は**<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Kz44Oz44OG44Kt44K544OI6ZW3IHwgQ29udGV4dCBMZW5ndGggfCBDb250ZXh0IFdpbmRvdw==">コンテキスト長</a>nのとき**$O(n^2)$に比例。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Kz44Oz44OG44Kt44K544OI6ZW3IHwgQ29udGV4dCBMZW5ndGggfCBDb250ZXh0IFdpbmRvdw==">コンテキスト長</a>が長いほど、長文の理解や生成が可能になるが、計算コストも増大する。

## 自己回帰 | Autoregression<a id="6Ieq5bex5Zue5biwIHwgQXV0b3JlZ3Jlc3Npb24="></a>

- 過去の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>系列 $x\_{1:t}$ を条件に、次の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a> $x\_{t+1}$ を逐次予測する生成方式。

$$
p(x\_{1:T}) = \\prod\_{t=1}^{T} p(x_t \\mid x\_{\\lt t})
$$

## Temperature | 温度パラメータ | 温度<a id="VGVtcGVyYXR1cmUgfCDmuKnluqbjg5Hjg6njg6Hjg7zjgr8gfCDmuKnluqY="></a>

- サンプリング分布のシャープさを制御するパラメータ。
- 対話の創造性・一貫性の調整する。
  - Tが大きいほど多様な応答が生成される。
  - Tが小さいほど決定的な応答が生成される。

$$
p'(x) = \\frac{\\exp(\\log p(x) / T)}{\\sum_j \\exp(\\log p(x_j) / T)}
$$

## FlashAttention<a id="Rmxhc2hBdHRlbnRpb24="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#U2VsZi1BdHRlbnRpb24gfCDoh6rlt7Hms6jmhI/mqZ/mp4s=">Self-Attention</a>を**メモリ効率よくGPUで計算**するアルゴリズム。
  - 行列演算でTilingして(=演算処理を小ブロックに分けて)、メモリアクセス局所性を高めるのと同じように、
  - Softmax演算も工夫してTilingを行っている。
- (参考): GPU と FlashAttension をちゃんと理解したい｜uchiiii <a href="https://zenn.dev/uchiiii/articles/306d0bb7ef67a7">https://zenn.dev/uchiiii/articles/306d0bb7ef67a7</a>

## Mixture of Experts (MoE)<a id="TWl4dHVyZSBvZiBFeHBlcnRzIChNb0Up"></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>のネットワークアーキテクチャの一種。
- 複数の専門家ネットワーク（Expert）を用意し、入力ごとに一部のみを動的に活性化させる。
- 追加のコストを抑えつつ<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5aSn6KaP5qih6KiA6Kqe44Oi44OH44OrfCBMYXJnZSBMYW5ndWFnZSBNb2RlbCB8IExMTQ==">LLM</a>のパラメータ総数を増やすための工夫。
- メリット:
  - 計算効率の改善。パラメータ÷{学習/<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#5o6o6KuWIHwgSW5mZXJlbmNl">推論</a>に必要な計算量}を低減できる。
- デメリット:
  - 学習の安定性。学習中、活性化されるExpertが偏ると上手く学習できない。

## Self-Attention | 自己注意機構<a id="U2VsZi1BdHRlbnRpb24gfCDoh6rlt7Hms6jmhI/mqZ/mp4s="></a>

- 入力<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>列内の各<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>同士が相互に関連度を計算し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/deep-learning.md#6YeN44G/IHwg6YeN44G/44OR44Op44Oh44O844K/IHwgV2VpZ2h0IHwgV2VpZ2h0IFBhcmFtZXRlcg==">重み</a>付き和を取る機構。

$$
\\text{Self-Atten}(Q,K,V) = \\text{softmax}\\left(\\frac{QK^\\top}{\\sqrt{d_k}}\\right)V
, \\text{where } Q=W_Qx, K=W_Kx, V=W_Vx
$$

- $n$: <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Kz44Oz44OG44Kt44K544OI6ZW3IHwgQ29udGV4dCBMZW5ndGggfCBDb250ZXh0IFdpbmRvdw==">コンテキスト長</a>
- $d_k$: モデルの次元数
- $x$: 入力<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>列(サイズ: $n \\times d_k$)
- $Q$: Query行列(サイズ:$n \\times d_k$), $W\_{Q}x$で計算される
- $K$: Key行列(サイズ:$n \\times d_k$), $W\_{K}x$で計算される
- $V$: Value行列(サイズ:$n \\times d_k$), $W\_{K}x$で計算される
- $QK^\\top$: <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwg44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIHwgQXR0ZW50aW9uIG1lY2hhbmlzbQ==">Attention</a>行列(サイズ:$n \\times n$)
