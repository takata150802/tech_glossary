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

## 推論 | Inference<a id="5o6o6KuWIHwgSW5mZXJlbmNl"></a>

- 学習済みモデルに対して<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OX44Ot44Oz44OX44OIIHwgUHJvbXB0">プロンプト</a>を与え、次の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>またはテキスト全体を生成させる処理。

## プロンプト | Prompt<a id="44OX44Ot44Oz44OX44OIIHwgUHJvbXB0"></a>

- モデルへの入力文。コンテキストや命令、質問などを含むことが多く、Zero-shotやFew-shotにも活用される。

## デコーダー | Decoder<a id="44OH44Kz44O844OA44O8IHwgRGVjb2Rlcg=="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>における出力生成側のネットワーク構造で、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#6Ieq5bex5Zue5biwIHwgQXV0b3JlZ3Jlc3NpdmU=">自己回帰</a>的に<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を予測する。

## RMSNorm | LayerNorm<a id="Uk1TTm9ybSB8IExheWVyTm9ybQ=="></a>

- 各レイヤーにおいて出力のスケーリングを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5q2j6KaP5YyWIHwgUmVndWxhcml6YXRpb24=">正規化</a>し勾配の安定性を高めるテクニック。

## 自己回帰 | Autoregressive<a id="6Ieq5bex5Zue5biwIHwgQXV0b3JlZ3Jlc3NpdmU="></a>

- 入力の過去の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を使って次の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>を逐次生成するモデル構造。GPT系列などが該当。

## コンテキスト長 | Context Length | Context Window<a id="44Kz44Oz44OG44Kt44K544OI6ZW3IHwgQ29udGV4dCBMZW5ndGggfCBDb250ZXh0IFdpbmRvdw=="></a>

- モデルが一度に処理可能な最大<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>数。大きいほど長文処理能力が向上するが、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwg44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIHwgQXR0ZW50aW9uIG1lY2hhbmlzbQ==">アテンション</a>の計算量が増大する。

## Temperature<a id="VGVtcGVyYXR1cmU="></a>

- モデルの出力の多様性を制御するパラメータ。高い値（例：1.0）は多様な応答を生成し、低い値（例：0.2）はより決定的な応答を生成する。
- 例：ChatGPTの温度パラメータを調整することで、よりクリエイティブな応答や、より一貫性のある応答を生成することができる。

## FlashAttention<a id="Rmxhc2hBdHRlbnRpb24="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwg44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIHwgQXR0ZW50aW9uIG1lY2hhbmlzbQ==">アテンション</a>計算をメモリアクセス最適化により高速化したアルゴリズム。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>のスケーラビリティを改善。

## Mixture of Experts | MoE<a id="TWl4dHVyZSBvZiBFeHBlcnRzIHwgTW9F"></a>

- 複数のサブネットワーク（専門家）を用意し、入力ごとに一部のみを動かすことで、計算量を抑えつつモデルの能力を拡張。

## Sparse Transformer<a id="U3BhcnNlIFRyYW5zZm9ybWVy"></a>

- 全<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>間の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwg44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIHwgQXR0ZW50aW9uIG1lY2hhbmlzbQ==">アテンション</a>ではなく、一部の接続のみ有効にすることで、計算量とメモリ使用を削減した<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>の変種。

## Self-Attention<a id="U2VsZi1BdHRlbnRpb24="></a>

- 入力系列内の全<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/nlp.md#44OI44O844Kv44OzIHwgVG9rZW4=">トークン</a>ペアに対し、クエリ（Q）、キー（K）、バリュー（V）の内積スコアをSoftmax<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/ai-general.md#5q2j6KaP5YyWIHwgUmVndWxhcml6YXRpb24=">正規化</a>して加重和を取る<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44Ki44OG44Oz44K344On44OzIHwg44Ki44OG44Oz44K344On44Oz5qmf5qeLIHwgQXR0ZW50aW9uIHwgQXR0ZW50aW9uIG1lY2hhbmlzbQ==">アテンション機構</a>。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md#44OI44Op44Oz44K544OV44Kp44O844Oe44O8IHwgVHJhbnNmb3JtZXI=">Transformer</a>の基盤であり、長距離依存関係の獲得に寄与する。
