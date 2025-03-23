<!-- 記事タイトル:用語解説集-計算機科学-アーキテクチャ-シミュレータ -->
<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md# -->

## アーキテクチャシミュレータ | Architecture Simulator 
- プロセッサの動作をモデル化し、実際のハードウェアを使わずにその性能や動作を予測・分析するツール
- 目的:
  - プロセッサの設計空間探索: 
    - プロセッサ設計における目標や制約(=性能、電力、面積、コスト)を満たす設計を見つけ出すこと。
    - 具体例なシミュレータは、対象の命令セットやシミュレーションの抽象度により様々。
    - パラメータはコア数、キャッシュ、バス幅、SIMD幅など
  - ソフトウェア開発環境の提供: 新しいプロセッサの開発中にソフトウェア開発を行う
- 具体例なシミュレータには以下のようなものがある。
  - gem5
  - Sniper
  - McPAT
  - MARSSx86
  - SimpleScalar
- シミュレーションの抽象度には以下のようなものがある。
  - Full-system simulation
  - User-level simulation
  - Functional simulation
  - Instruction-Level simulation
  - サイクルアキュレート | Cycle accurate simulation
  - Event-driven simulation
  - Trace-driven simulation

## gem5 
- OSSのシミュレータ
  - <a href="https://github.com/gem5/gem5/"> https://github.com/gem5/gem5/ </a>
  - BSD 3-Clause
- 様々な命令セットをサポート(x86、ARM、MIPS、Alpha、PPC、SPARC)
- Full-system simulation、サイクルアキュレート
- マルチコアサポート
- アカデミアで設計空間探索に広く利用されている

## MARSSx86 
- 命令セットはx86-64
- User-level simulation、Functional simulationだが一部はサイクルアキュレート
- マルチコアサポート
- 現代のマルチコアx86プロセッサの詳細なモデリングをサポート

## Multi2Sim 
- 様々な命令セットをサポート(x86、AMD、ARM、MIPS32、Evergreen、NVIDIA Fermi)
- User-level simulation、粒度は不明
- マルチコアサポート
- CPU-GPUシミュレーションに用いられる

## Sniper 
- 命令セットはx86、RISC-V
- User-level simulation、粒度は不明
- マルチコアサポート

## PTLsim 
- 命令セットはx86
- Full-system simulation、サイクルアキュレート
- マルチコアサポート
- AMDプロセッサのシミュレーションに用いられる

## ZSim 
- 命令セットはx86-64
- User-level simulation、粒度は不明
- マルチコアサポート

## McPAT 
- 様々な命令セットをサポート(x86、ARM、Alpha、SPARC)
- 電力、面積の評価に用いられる サイクルアキュレート　
- マルチコアサポート
- Multi-core Power, Area, and Timingの略

## SimpleScalar 
- 様々な命令セットをサポート(x86、ARM、Alpha、Pisa)
- User-level simulation、粒度は様々
- マルチコア非対応

## Full-system simulation 
- コンピュータシステムの全体をシミュレーションする
  - ユーザーランドで動作するプログラムだけでなく、OSやデバイスドライバを含む
  - プロセッサ内部だけでなく、メモリシステムやI/Oデバイスを含む
- 主にオペレーティングシステムなどシステムソフトウェアの研究に用いられる

## User-level simulation 
- オペレーティングシステムのカーネルやデバイスドライバーを含まない、ユーザーランドで動作するプログラムのみを対象とするシミュレーション
- いわゆるOSなどシステムソフトウェアではなく、アプリケーションの性能やアルゴリズムの良し悪しに関心がる場合に使う
  
## Functional simulation 
- 正確さが劣っても良いので高速なシミュレーションを行いたい場合に用いる。
- 特定の入力に対する出力が期待どおりであるかどうかを確認することに焦点を当てていますが、実行にかかる時間やサイクル数は考慮しない。
- CPUが対象の場合は、Instruction-Level simulation とほぼ同義。

## Instruction-Level simulation 
- 対象とする命令セットアーキテクチャの各命令の動作を再現することに重点を置く。
- サイクル数等詳細な情報は提供しない。
- 新しい命令セットアーキテクチャを開発する際やに用いる。
  - あるプログラムで実行された命令毎の総数やメモリアクセスの局所性を調べるのに使う。

## サイクルアキュレート | Cycle accurate simulation 
- 対象の動作をクロックサイクル単位で正確にモデル化する。
- OS全体やコンピュータシステム全体を対象とすると、シミュレーションが現実的な時間で完了しない。

## Event-driven simulation 
- コンピュータシステム内で発生するイベントを用いる方法
  - イベントとは、命令のフェッチ、メモリアクセス、I/Oアクセスなど

## Trace-driven simulation 
- 実機や他のシミュレータから採取したトレースデータを用いる方法
  - トレースデータとは、命令シーケンスやメモリアクセスパターン
- 特定のアプリケーション、ワークロードの性能分析や、コンピュータシステムの挙動の分析に用いる

---

VLSI設計の文脈における、シミュレーションの抽象度には下記の3つがある。

1. ビヘイビアレベル | Behaivioral-level
2. RTL | Register Transfer Level
3. ゲートレベル | Gate-Level

## ビヘイビアレベル | Behaivioral-level 
- VLSI設計の文脈における、シミュレーションの抽象度の1つ
  - 回路が何をするかを記載する。具体例な実装方法には踏み込まない。サイクルアキュレートではない。
- 目的は、VLSI設計の初期段階における、設計対象の明確化。

## RTL | Register Transfer Level  
- VLSI設計の文脈における、シミュレーションの抽象度の1つ
  - 一般に、論理回路設計の最終成果物は、この抽象度で記述される。より低い抽象度であるネットリスト(=ゲートレベルの記述)には論理論理合成によってなされ、人手では行わない。
  - この抽象度は、任意の1サイクルにおける記憶素子から記憶素子への論理関数を記述したものである。
- 目的は、論理回路設計のデバック・検証。

## ゲートレベル | Gate-Level  
- VLSI設計の文脈における、シミュレーションの抽象度の1つ
  - 回路をネットリストで記述し(=論理ゲートのスタンダードセル, フリップフロップ, RAM等で記述し)、
  - クロックサイクルより細かいタイムスケールでシミュレーションする
- 目的は、電力評価、動的タイミング解析。
