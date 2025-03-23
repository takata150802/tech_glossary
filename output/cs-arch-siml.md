<!-- 記事タイトル:用語解説集-計算機科学-アーキテクチャ-シミュレータ -->

<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md# -->

## アーキテクチャシミュレータ | Architecture Simulator<a id="44Ki44O844Kt44OG44Kv44OB44Oj44K344Of44Ol44Os44O844K/IHwgQXJjaGl0ZWN0dXJlIFNpbXVsYXRvcg=="></a>

- プロセッサの動作をモデル化し、実際のハードウェアを使わずにその性能や動作を予測・分析するツール
- 目的:
  - プロセッサの設計空間探索:
    - プロセッサ設計における目標や制約(=性能、電力、面積、コスト)を満たす設計を見つけ出すこと。
    - 具体例なシミュレータは、対象の命令セットやシミュレーションの抽象度により様々。
    - パラメータはコア数、キャッシュ、バス幅、SIMD幅など
  - ソフトウェア開発環境の提供: 新しいプロセッサの開発中にソフトウェア開発を行う
- 具体例なシミュレータには以下のようなものがある。
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#Z2VtNQ==">gem5</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#U25pcGVy">Sniper</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#TWNQQVQ=">McPAT</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#TUFSU1N4ODY=">MARSSx86</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#U2ltcGxlU2NhbGFy">SimpleScalar</a>
- シミュレーションの抽象度には以下のようなものがある。
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#RnVsbC1zeXN0ZW0gc2ltdWxhdGlvbg==">Full-system simulation</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#VXNlci1sZXZlbCBzaW11bGF0aW9u">User-level simulation</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#RnVuY3Rpb25hbCBzaW11bGF0aW9u">Functional simulation</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#SW5zdHJ1Y3Rpb24tTGV2ZWwgc2ltdWxhdGlvbg==">Instruction-Level simulation</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44K144Kk44Kv44Or44Ki44Kt44Ol44Os44O844OIIHwgQ3ljbGUgYWNjdXJhdGUgc2ltdWxhdGlvbg==">サイクルアキュレート</a> | <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44K144Kk44Kv44Or44Ki44Kt44Ol44Os44O844OIIHwgQ3ljbGUgYWNjdXJhdGUgc2ltdWxhdGlvbg==">Cycle accurate simulation</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#RXZlbnQtZHJpdmVuIHNpbXVsYXRpb24=">Event-driven simulation</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#VHJhY2UtZHJpdmVuIHNpbXVsYXRpb24=">Trace-driven simulation</a>

## gem5<a id="Z2VtNQ=="></a>

- OSSのシミュレータ
  - <a href="https://github.com/gem5/gem5/"> https://github.com/gem5/gem5/ </a>
  - BSD 3-Clause
- 様々な命令セットをサポート(x86、ARM、MIPS、Alpha、PPC、SPARC)
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#RnVsbC1zeXN0ZW0gc2ltdWxhdGlvbg==">Full-system simulation</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44K144Kk44Kv44Or44Ki44Kt44Ol44Os44O844OIIHwgQ3ljbGUgYWNjdXJhdGUgc2ltdWxhdGlvbg==">サイクルアキュレート</a>
- マルチコアサポート
- アカデミアで設計空間探索に広く利用されている

## MARSSx86<a id="TUFSU1N4ODY="></a>

- 命令セットはx86-64
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#VXNlci1sZXZlbCBzaW11bGF0aW9u">User-level simulation</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#RnVuY3Rpb25hbCBzaW11bGF0aW9u">Functional simulation</a>だが一部は<a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44K144Kk44Kv44Or44Ki44Kt44Ol44Os44O844OIIHwgQ3ljbGUgYWNjdXJhdGUgc2ltdWxhdGlvbg==">サイクルアキュレート</a>
- マルチコアサポート
- 現代のマルチコアx86プロセッサの詳細なモデリングをサポート

## Multi2Sim<a id="TXVsdGkyU2lt"></a>

- 様々な命令セットをサポート(x86、AMD、ARM、MIPS32、Evergreen、NVIDIA Fermi)
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#VXNlci1sZXZlbCBzaW11bGF0aW9u">User-level simulation</a>、粒度は不明
- マルチコアサポート
- CPU-GPUシミュレーションに用いられる

## Sniper<a id="U25pcGVy"></a>

- 命令セットはx86、RISC-V
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#VXNlci1sZXZlbCBzaW11bGF0aW9u">User-level simulation</a>、粒度は不明
- マルチコアサポート

## PTLsim<a id="UFRMc2lt"></a>

- 命令セットはx86
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#RnVsbC1zeXN0ZW0gc2ltdWxhdGlvbg==">Full-system simulation</a>、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44K144Kk44Kv44Or44Ki44Kt44Ol44Os44O844OIIHwgQ3ljbGUgYWNjdXJhdGUgc2ltdWxhdGlvbg==">サイクルアキュレート</a>
- マルチコアサポート
- AMDプロセッサのシミュレーションに用いられる

## ZSim<a id="WlNpbQ=="></a>

- 命令セットはx86-64
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#VXNlci1sZXZlbCBzaW11bGF0aW9u">User-level simulation</a>、粒度は不明
- マルチコアサポート

## McPAT<a id="TWNQQVQ="></a>

- 様々な命令セットをサポート(x86、ARM、Alpha、SPARC)
- 電力、面積の評価に用いられる <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44K144Kk44Kv44Or44Ki44Kt44Ol44Os44O844OIIHwgQ3ljbGUgYWNjdXJhdGUgc2ltdWxhdGlvbg==">サイクルアキュレート</a>
- マルチコアサポート
- Multi-core Power, Area, and Timingの略

## SimpleScalar<a id="U2ltcGxlU2NhbGFy"></a>

- 様々な命令セットをサポート(x86、ARM、Alpha、Pisa)
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#VXNlci1sZXZlbCBzaW11bGF0aW9u">User-level simulation</a>、粒度は様々
- マルチコア非対応

## Full-system simulation<a id="RnVsbC1zeXN0ZW0gc2ltdWxhdGlvbg=="></a>

- コンピュータシステムの全体をシミュレーションする
  - ユーザーランドで動作するプログラムだけでなく、OSやデバイスドライバを含む
  - プロセッサ内部だけでなく、メモリシステムやI/Oデバイスを含む
- 主にオペレーティングシステムなどシステムソフトウェアの研究に用いられる

## User-level simulation<a id="VXNlci1sZXZlbCBzaW11bGF0aW9u"></a>

- オペレーティングシステムのカーネルやデバイスドライバーを含まない、ユーザーランドで動作するプログラムのみを対象とするシミュレーション
- いわゆるOSなどシステムソフトウェアではなく、アプリケーションの性能やアルゴリズムの良し悪しに関心がる場合に使う

## Functional simulation<a id="RnVuY3Rpb25hbCBzaW11bGF0aW9u"></a>

- 正確さが劣っても良いので高速なシミュレーションを行いたい場合に用いる。
- 特定の入力に対する出力が期待どおりであるかどうかを確認することに焦点を当てていますが、実行にかかる時間やサイクル数は考慮しない。
- CPUが対象の場合は、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#SW5zdHJ1Y3Rpb24tTGV2ZWwgc2ltdWxhdGlvbg==">Instruction-Level simulation</a> とほぼ同義。

## Instruction-Level simulation<a id="SW5zdHJ1Y3Rpb24tTGV2ZWwgc2ltdWxhdGlvbg=="></a>

- 対象とする命令セットアーキテクチャの各命令の動作を再現することに重点を置く。
- サイクル数等詳細な情報は提供しない。
- 新しい命令セットアーキテクチャを開発する際やに用いる。
  - あるプログラムで実行された命令毎の総数やメモリアクセスの局所性を調べるのに使う。

## サイクルアキュレート | Cycle accurate simulation<a id="44K144Kk44Kv44Or44Ki44Kt44Ol44Os44O844OIIHwgQ3ljbGUgYWNjdXJhdGUgc2ltdWxhdGlvbg=="></a>

- 対象の動作をクロックサイクル単位で正確にモデル化する。
- OS全体やコンピュータシステム全体を対象とすると、シミュレーションが現実的な時間で完了しない。

## Event-driven simulation<a id="RXZlbnQtZHJpdmVuIHNpbXVsYXRpb24="></a>

- コンピュータシステム内で発生するイベントを用いる方法
  - イベントとは、命令のフェッチ、メモリアクセス、I/Oアクセスなど

## Trace-driven simulation<a id="VHJhY2UtZHJpdmVuIHNpbXVsYXRpb24="></a>

- 実機や他のシミュレータから採取したトレースデータを用いる方法
  - トレースデータとは、命令シーケンスやメモリアクセスパターン
- 特定のアプリケーション、ワークロードの性能分析や、コンピュータシステムの挙動の分析に用いる

______________________________________________________________________

VLSI設計の文脈における、シミュレーションの抽象度には下記の3つがある。

1. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44OT44OY44Kk44OT44Ki44Os44OZ44OrIHwgQmVoYWl2aW9yYWwtbGV2ZWw=">ビヘイビアレベル</a> | <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44OT44OY44Kk44OT44Ki44Os44OZ44OrIHwgQmVoYWl2aW9yYWwtbGV2ZWw=">Behaivioral-level</a>
1. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#UlRMIHwgUmVnaXN0ZXIgVHJhbnNmZXIgTGV2ZWw=">RTL</a> | <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#UlRMIHwgUmVnaXN0ZXIgVHJhbnNmZXIgTGV2ZWw=">Register Transfer Level</a>
1. <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44Ky44O844OI44Os44OZ44OrIHwgR2F0ZS1MZXZlbA==">ゲートレベル</a> | <a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44Ky44O844OI44Os44OZ44OrIHwgR2F0ZS1MZXZlbA==">Gate-Level</a>

## ビヘイビアレベル | Behaivioral-level<a id="44OT44OY44Kk44OT44Ki44Os44OZ44OrIHwgQmVoYWl2aW9yYWwtbGV2ZWw="></a>

- VLSI設計の文脈における、シミュレーションの抽象度の1つ
  - 回路が何をするかを記載する。具体例な実装方法には踏み込まない。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44K144Kk44Kv44Or44Ki44Kt44Ol44Os44O844OIIHwgQ3ljbGUgYWNjdXJhdGUgc2ltdWxhdGlvbg==">サイクルアキュレート</a>ではない。
- 目的は、VLSI設計の初期段階における、設計対象の明確化。

## RTL | Register Transfer Level<a id="UlRMIHwgUmVnaXN0ZXIgVHJhbnNmZXIgTGV2ZWw="></a>

- VLSI設計の文脈における、シミュレーションの抽象度の1つ
  - 一般に、論理回路設計の最終成果物は、この抽象度で記述される。より低い抽象度であるネットリスト(=<a href="https://github.com/takata150802/tech_glossary/blob/main/output/cs-arch-siml.md#44Ky44O844OI44Os44OZ44OrIHwgR2F0ZS1MZXZlbA==">ゲートレベル</a>の記述)には論理論理合成によってなされ、人手では行わない。
  - この抽象度は、任意の1サイクルにおける記憶素子から記憶素子への論理関数を記述したものである。
- 目的は、論理回路設計のデバック・検証。

## ゲートレベル | Gate-Level<a id="44Ky44O844OI44Os44OZ44OrIHwgR2F0ZS1MZXZlbA=="></a>

- VLSI設計の文脈における、シミュレーションの抽象度の1つ
  - 回路をネットリストで記述し(=論理ゲートのスタンダードセル, フリップフロップ, RAM等で記述し)、
  - クロックサイクルより細かいタイムスケールでシミュレーションする
- 目的は、電力評価、動的タイミング解析。
