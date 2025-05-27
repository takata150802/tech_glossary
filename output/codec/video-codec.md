<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md# -->

## ビットストリーム | Bitstream<a id="44OT44OD44OI44K544OI44Oq44O844OgIHwgQml0c3RyZWFt"></a>

- メディアプレイヤー(動画プレーヤーや音楽プレーヤー)で再生できるメディアファイルのこと。
- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#44Kz44Oz44OG44OKIHwgQ29udGFpbmVy">コンテナ</a>から構成される。

## コンテナ | Container<a id="44Kz44Oz44OG44OKIHwgQ29udGFpbmVy"></a>

- ビデオとオーディオのデータに加え、字幕、メタデータ、チャプターマーカーなどの追加情報を保持するデジタルファイル形式
- 1つ以上の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#RWxlbWVudGFyeSBzdHJlYW0=">Elementary stream</a>を保持する。
- 具体例:
  - MP4
  - MKV
  - AVI
  - MOV
- (参考):
  - https://wiki.x266.mov/docs/introduction/terminology#container

## Elementary stream<a id="RWxlbWVudGFyeSBzdHJlYW0="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#56ym5Y+35YyWIHwg44Ko44Oz44Kz44O844OJIHwgRW5jb2Rpbmc=">エンコード</a>されたオーディオ、ビデオ、または字幕トラックのこと。

## コーデック | Codec<a id="44Kz44O844OH44OD44KvIHwgQ29kZWM="></a>

- 音声や動画などのデータを<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#56ym5Y+35YyWIHwg44Ko44Oz44Kz44O844OJIHwgRW5jb2Rpbmc=">エンコード</a>及び<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#5b6p5Y+3IHwg44OH44Kz44O844OJIHwgRGVjb2Rpbmc=">デコード</a>する技術やソフトウェア/ハードウェアの総称。
- COmpressor-DECompressorの略。
- 具体例:
  - 画像<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#44Kz44O844OH44OD44KvIHwgQ29kZWM=">コーデック</a>
  - 音声<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#44Kz44O844OH44OD44KvIHwgQ29kZWM=">コーデック</a>
  - <a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#5YuV55S744Kz44O844OH44OD44KvIHwgVmlkZW8gQ29kZWM=">動画コーデック</a>

## 動画コーデック | Video Codec<a id="5YuV55S744Kz44O844OH44OD44KvIHwgVmlkZW8gQ29kZWM="></a>

- 動画の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#44Kz44O844OH44OD44KvIHwgQ29kZWM=">コーデック</a>
- 具体例:
  - Motion JPEG
  - H.264/MPEG-4 AVC
  - H.265/HEVC
  - H.266/VVC
  - VP9
  - AV1
- (参考):
  - https://ja.wikipedia.org/wiki/<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#44Kz44O844OH44OD44KvIHwgQ29kZWM=">コーデック</a>#動画圧縮の<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#44Kz44O844OH44OD44KvIHwgQ29kZWM=">コーデック</a>
  - https://en.wikipedia.org/wiki/Comparison_of_video_codecs
  - https://en.wikipedia.org/wiki/List_of_codecs#Video_compression_formats

## 可逆圧縮 | Lossless<a id="5Y+v6YCG5Zyn57iuIHwgTG9zc2xlc3M="></a>

- 圧縮されたデータから元のデータを完全に復元できるデータ圧縮手法
- 具体例:
  - ランレングス<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#56ym5Y+35YyWIHwg44Ko44Oz44Kz44O844OJIHwgRW5jb2Rpbmc=">符号化</a>
  - ハフマン<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#56ym5Y+35YyWIHwg44Ko44Oz44Kz44O844OJIHwgRW5jb2Rpbmc=">符号化</a>

## 非可逆圧縮 | Lossy<a id="6Z2e5Y+v6YCG5Zyn57iuIHwgTG9zc3k="></a>

- 人間の感覚の限界、忠実度指標、または訴求力指標を利用して、重要度の低いと判断される情報を破棄して圧縮率を向上させるデータ圧縮手法。
- 圧縮されたデータから元のデータを完全に復元することはできない。

## 符号化 | エンコード | Encoding<a id="56ym5Y+35YyWIHwg44Ko44Oz44Kz44O844OJIHwgRW5jb2Rpbmc="></a>

- 生の映像信号を圧縮し、ストレージまたは転送に適した形式に変換するプロセス。動き補償、変換（例：DCT）、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md#6YeP5a2Q5YyWIHwgUXVhbnRpemF0aW9u">量子化</a>、CABAC等のエントロピー<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#56ym5Y+35YyWIHwg44Ko44Oz44Kz44O844OJIHwgRW5jb2Rpbmc=">符号化</a>を含む多段階処理であり、圧縮効率と品質のトレードオフが鍵となる。

## 復号 | デコード | Decoding<a id="5b6p5Y+3IHwg44OH44Kz44O844OJIHwgRGVjb2Rpbmc="></a>

- 圧縮された<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#44OT44OD44OI44K544OI44Oq44O844OgIHwgQml0c3RyZWFt">ビットストリーム</a>を解析し、近似的に元の映像信号を復元するプロセス。逆変換、逆<a href="https://github.com/takata150802/tech_glossary/blob/main/output/ai/llm-optimization.md#6YeP5a2Q5YyWIHwgUXVhbnRpemF0aW9u">量子化</a>、動き補償再構成、補間フィルタ適用などを含む。

## ビットレート | Bitrate<a id="44OT44OD44OI44Os44O844OIIHwgQml0cmF0ZQ=="></a>

- 単位時間あたりの転送データ量（通常bps, kbps, Mbpsで表現）。圧縮率、画質、帯域幅の指標となる。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#44Kz44O844OH44OD44KvIHwgQ29kZWM=">コーデック</a>設定の根幹であり、可変<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#44OT44OD44OI44Os44O844OIIHwgQml0cmF0ZQ==">ビットレート</a>（VBR）や固定<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#44OT44OD44OI44Os44O844OIIHwgQml0cmF0ZQ==">ビットレート</a>（CBR）戦略と密接に関係する。

## フレームレート | Frame Rate<a id="44OV44Os44O844Og44Os44O844OIIHwgRnJhbWUgUmF0ZQ=="></a>

- 単位時間あたりのフレーム数。<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#ZnBzIHwgRnJhbWVzIFBlciBTZWNvbmQ=">fps</a>（frames per second）で表現され、典型値には24, 30, 60<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#ZnBzIHwgRnJhbWVzIFBlciBTZWNvbmQ=">fps</a>などがある。滑らかさ、帯域、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#56ym5Y+35YyWIHwg44Ko44Oz44Kz44O844OJIHwgRW5jb2Rpbmc=">エンコード</a>負荷に直接影響する。

## fps | Frames Per Second<a id="ZnBzIHwgRnJhbWVzIFBlciBTZWNvbmQ="></a>

- <a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#44OV44Os44O844Og44Os44O844OIIHwgRnJhbWUgUmF0ZQ==">フレームレート</a>の単位。1秒間に表示または処理されるフレームの数。映画は24<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#ZnBzIHwgRnJhbWVzIFBlciBTZWNvbmQ=">fps</a>、テレビは30<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#ZnBzIHwgRnJhbWVzIFBlciBTZWNvbmQ=">fps</a>、ゲームやスポーツは60<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#ZnBzIHwgRnJhbWVzIFBlciBTZWNvbmQ=">fps</a>以上が一般的。

## 解像度 | Resolution<a id="6Kej5YOP5bqmIHwgUmVzb2x1dGlvbg=="></a>

- 映像フレームの画素数を縦横で定義した指標。典型的には横×縦の形式（例：1920×1080）で表される。映像のディテール表現能力に直結し、<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#56ym5Y+35YyWIHwg44Ko44Oz44Kz44O844OJIHwgRW5jb2Rpbmc=">符号化</a>効率や帯域要求、ストレージ容量にも影響を与える。4Kや8KなどはITU-R BT.2020に準拠した高<a href="https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md#6Kej5YOP5bqmIHwgUmVzb2x1dGlvbg==">解像度</a>規格である。

- (参考):

  - http://www.johoka.info/index.php?action=common_download_main&upload_id=1733&nc_session=15c6a045ccf89999d30ba1dad87b7ef9

## Muxer<a id="TXV4ZXI="></a>

## Demuxer<a id="RGVtdXhlcg=="></a>

## Transcoding<a id="VHJhbnNjb2Rpbmc="></a>

## RDO<a id="UkRP"></a>

## Psychovisual quality<a id="UHN5Y2hvdmlzdWFsIHF1YWxpdHk="></a>
