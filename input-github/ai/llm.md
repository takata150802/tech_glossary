<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm.md# -->


## 大規模言語モデル| Large Language Model | LLM 
- 大規模な計算資源を使い、一般的にTransformerベースの大規模な言語モデルを、Web上から収集した大規模なテキストデータで学習させたモデル。
  - 2010年代、**主に画像認識や物体検出を行う画像系の深層学習モデルの研究開発が注目を集め、本来ゲーミング用途に使われるGPUが深層学習モデルの研究開発に用いられるようになった(GPGPUの一環)**。その後、Google社主導のTensorFlowやMeta社(旧Facebook社)主導のPyTorchといった深層学習フレームワークがOSSでライセンスの範囲内で自由に利用できることも手伝って、**大規模なGPU計算資源を使った深層学習モデルの学習が様々な研究機関・大学・企業で行われるようになった。**
  - 2017年、**Google社の論文「Attention Is All You Need」にて提唱された自然言語系の深層学習モデルTransformerは、自然言語処理、特に機械翻訳の分野で優れた性能を示し、自然言語処理のおける深層学習のブレイクスルー**となった。この深層学習モデルTransformerの最も重要なアイディアであるアテンション機構は、ほぼ全ての著名なLLMが継承しているアイディアであるので、本論文はLLM分野における基礎的な論文とみなされている。
  - 2018年、OpenAI社の論文「Improving Language Understanding by Generative Pre-Training」で初めて、GPT(=いわゆるLLMの事前学習)が提唱された。従来、自然言語処理系の深層学習モデルは人手でラベル付けしたデータセットで教師あり学習しており、人手でのラベル付けは高コストなため大規模なデータセット構築の制約となっていた。一方で、**GPT(=いわゆるLLMの事前学習)は教師なし学習のためWeb上から収集した膨大なテキストデータを深層学習モデルに学習させることを実現し、大きなブレイクスルー**となった。2022年、OpenAI社がChatGPT(=LLMを用いたChatBotのWebサービス)がリリースされると世間の注目を集め、広く認知されるに至った。2025年現在、北米/中国IT大手が研究開発を牽引し、多くのプロダクト・サービスにLLMが投入され商業的成功を収めている。

**著名なLLM:**
- LLMの研究開発競争は激しく、著名なLLMは日々アップデートが必要なため下記のサーベイ論文、もしくはリーダーボードを参照。
  - サーベイ論文: 
    - Zhao, Wayne Xin, et al. "A survey of large language models." arXiv preprint arXiv:2303.18223 1.2 (2023).　https://arxiv.org/abs/2303.18223
      - 初版version1は2023年3月31日だが、v2,v3...とアップデートされており、version16が2025年3月11日に公開。
      - ※ 下記図は、本サーベイ論文のFigure.3を引用したものです。
        - ![](./llm.md-ASurveyOfLLM_figure3.png)

## リーダーボード | LLMリーダーボード | Leaderboard | LLM Leaderboard
- 主にLLMや画像生成AIの分野で、様々なモデルの性能を客観的に比較・評価するオンラインプラットフォーム
- 具体例:
  - Chatbot Arena: 
    - <a href="https://lmarena.ai/leaderboard">https://lmarena.ai/leaderboard</a>
    - LMArenaによるリーダーボード。
    - **ユーザー投票**でランキングを決める(定量評価も大事だが、ユーザーがどう感じたか?が最も重要というスタンス)。
    - 著名な公開モデルだけでなく、GPT-4oなど**クローズドな商用モデル**もランキングに含まれている。
  - Open LLM Leaderboard: 
    - <a href="https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard">https://huggingface.co/spaces/open-llm-leaderboard/open_llm_leaderboard</a>
    - **Hugging Face社による**主に公開モデルのリーダーボード
  - Swallow LLM Leaderboard v2
    - <a href="https://swallow-llm.github.io/evaluation/index.ja.html">https://swallow-llm.github.io/evaluation/index.ja.html</a>
    - 東京科学大学(旧:東工大)岡崎研・横田研 Swallowプロジェクトが、日本語に強いLLMの開発と並行して、公開されているLLMの評価実験を独自に進めているもの。**日本語の**評価タスク定量評価が含まれている。
  - Nejumi LLMリーダーボード3
    - <a href="https://wandb.ai/wandb-japan/llm-leaderboard3/reports/Nejumi-LLM-3--Vmlldzo3OTg2NjM2">https://wandb.ai/wandb-japan/llm-leaderboard3/reports/Nejumi-LLM-3--Vmlldzo3OTg2NjM2</a>
    - WandB社によるリーダーボード。**日本語の**評価タスク定量評価が含まれている。
    - 著名な公開モデルだけでなく、GPT-4oなど**クローズドな商用モデル**もランキングに含まれている。
  - Open Japanese LLM Leaderboard
    - <a href="https://huggingface.co/spaces/llm-jp/open-japanese-llm-leaderboard">https://huggingface.co/spaces/llm-jp/open-japanese-llm-leaderboard</a>
    - LLM-jp によるリーダーボード。 評価ツール llm-jp-eval を活用し、16種類のタスクで日本語の大規模言語モデルを評価している。

## Attention is all you need
- Vaswani, Ashish, et al. "Attention is all you need." Advances in neural information processing systems 30 (2017). https://arxiv.org/abs/1706.03762
- 2017年、Google社の論文
- 本論文にて提唱された自然言語系の深層学習モデルTransformerは、自然言語処理、特に機械翻訳の分野で優れた性能を示し、自然言語処理のおける深層学習のブレイクスルーとなった
- この深層学習モデルTransformerの最も重要なアイディアであるアテンション機構は、ほぼ全ての著名なLLMが継承しているアイディアであるので、本論文はLLM分野における基礎的な論文とみなされている。

## トランスフォーマー | Transformer
- 2017年、Google社の論文「Attention is all you need」にて提唱された自然言語系の深層学習モデル
  - 自然言語処理、特に機械翻訳の分野で優れた性能を示し、自然言語処理のおける深層学習のブレイクスルーとなった
  - 本モデルの最も重要なアイディアであるアテンション機構は、ほぼ全ての著名なLLMが継承している

- Hugging Face社によるOSSの深層学習ライブラリの1つ。
  - 自然言語処理に限らず、コンピュータビジョン、音声処理、マルチモーダルタスクの最先端のモデルの定義、学習、推論に用いられる
  - PyTorch、TensorFlow、JAXといった主要深層学習フレームワークに対応している

## アテンション | アテンション機構 | Attention | Attention mechanism
- 自然言語処理で良く用いられる深層学習モデルの構造の1種。
- 著名な自然言語処理系の深層学習モデルTransformerの最も重要なアイディアで、ほぼ全ての著名なLLMが継承しているアイディアである

- (引用元): <a href="https://speakerdeck.com/chokkan/20230327_riken_llm?slide=14">https://speakerdeck.com/chokkan/20230327_riken_llm?slide=14</a>
  - ![alt text](./llm.md.Transformer_0.png)

## 推論 | Inference	
- 学習済みモデルに対してプロンプトを与え、次のトークンまたはテキスト全体を生成させる処理。

## プロンプト | Prompt
- モデルへの入力文。コンテキストや命令、質問などを含むことが多く、Zero-shotやFew-shotにも活用される。

## デコーダー | Decoder
- Transformerにおける出力生成側のネットワーク構造で、自己回帰的にトークンを予測する。

## RMSNorm | LayerNorm
- 各レイヤーにおいて出力のスケーリングを正規化し勾配の安定性を高めるテクニック。

## 自己回帰 | Autoregressive
- 入力の過去のトークンを使って次のトークンを逐次生成するモデル構造。GPT系列などが該当。

## コンテキスト長 | Context Length | Context Window
- モデルが一度に処理可能な最大トークン数。大きいほど長文処理能力が向上するが、アテンションの計算量が増大する。

## Temperature
- モデルの出力の多様性を制御するパラメータ。高い値（例：1.0）は多様な応答を生成し、低い値（例：0.2）はより決定的な応答を生成する。
- 例：ChatGPTの温度パラメータを調整することで、よりクリエイティブな応答や、より一貫性のある応答を生成することができる。

## FlashAttention
- アテンション計算をメモリアクセス最適化により高速化したアルゴリズム。Transformerのスケーラビリティを改善。

## Mixture of Experts | MoE
- 複数のサブネットワーク（専門家）を用意し、入力ごとに一部のみを動かすことで、計算量を抑えつつモデルの能力を拡張。

## Sparse Transformer
- 全トークン間のアテンションではなく、一部の接続のみ有効にすることで、計算量とメモリ使用を削減したTransformerの変種。
## Self-Attention
- 入力系列内の全トークンペアに対し、クエリ（Q）、キー（K）、バリュー（V）の内積スコアをSoftmax正規化して加重和を取るアテンション機構。Transformerの基盤であり、長距離依存関係の獲得に寄与する。
