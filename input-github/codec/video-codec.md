<!-- 記事URL:https://github.com/takata150802/tech_glossary/blob/main/output/codec/video-codec.md# -->

## ビットストリーム | Bitstream
- メディアプレイヤー(動画プレーヤーや音楽プレーヤー)で再生できるメディアファイルのこと。
- コンテナから構成される。

## コンテナ | Container
- ビデオとオーディオのデータに加え、字幕、メタデータ、チャプターマーカーなどの追加情報を保持するデジタルファイル形式
- 1つ以上のElementary streamを保持する。
- 具体例:
  - MP4
  - MKV
  - AVI
  - MOV
- (参考):
  - https://wiki.x266.mov/docs/introduction/terminology#container

## Elementary stream
- エンコードされたオーディオ、ビデオ、または字幕トラックのこと。

## コーデック | Codec
- 音声や動画などのデータをエンコード及びデコードする技術やソフトウェア/ハードウェアの総称。
- COmpressor-DECompressorの略。
- 具体例:
  - 画像コーデック
  - 音声コーデック
  - 動画コーデック

## 動画コーデック | Video Codec
- 動画のコーデック
- 具体例:
  - Motion JPEG
  - H.264/MPEG-4 AVC
  - H.265/HEVC
  - H.266/VVC
  - VP9
  - AV1
- (参考):
  - https://ja.wikipedia.org/wiki/コーデック#動画圧縮のコーデック
  - https://en.wikipedia.org/wiki/Comparison_of_video_codecs
  - https://en.wikipedia.org/wiki/List_of_codecs#Video_compression_formats

## 可逆圧縮 | Lossless
- 圧縮されたデータから元のデータを完全に復元できるデータ圧縮手法
- 具体例:
  - ランレングス符号化
  - ハフマン符号化

## 非可逆圧縮 | Lossy
- 人間の感覚の限界、忠実度指標、または訴求力指標を利用して、重要度の低いと判断される情報を破棄して圧縮率を向上させるデータ圧縮手法。
- 圧縮されたデータから元のデータを完全に復元することはできない。

## 符号化 | エンコード | Encoding
- 生の映像信号を圧縮し、ストレージまたは転送に適した形式に変換するプロセス。動き補償、変換（例：DCT）、量子化、CABAC等のエントロピー符号化を含む多段階処理であり、圧縮効率と品質のトレードオフが鍵となる。

## 復号 | デコード | Decoding
- 圧縮されたビットストリームを解析し、近似的に元の映像信号を復元するプロセス。逆変換、逆量子化、動き補償再構成、補間フィルタ適用などを含む。

## ビットレート | Bitrate
- 単位時間あたりの転送データ量（通常bps, kbps, Mbpsで表現）。圧縮率、画質、帯域幅の指標となる。コーデック設定の根幹であり、可変ビットレート（VBR）や固定ビットレート（CBR）戦略と密接に関係する。

## フレームレート | Frame Rate
- 単位時間あたりのフレーム数。fps（frames per second）で表現され、典型値には24, 30, 60fpsなどがある。滑らかさ、帯域、エンコード負荷に直接影響する。

## fps | Frames Per Second
- フレームレートの単位。1秒間に表示または処理されるフレームの数。映画は24fps、テレビは30fps、ゲームやスポーツは60fps以上が一般的。

## 解像度 | Resolution
- 映像フレームの画素数を縦横で定義した指標。典型的には横×縦の形式（例：1920×1080）で表される。映像のディテール表現能力に直結し、符号化効率や帯域要求、ストレージ容量にも影響を与える。4Kや8KなどはITU-R BT.2020に準拠した高解像度規格である。

- (参考):
  - http://www.johoka.info/index.php?action=common_download_main&upload_id=1733&nc_session=15c6a045ccf89999d30ba1dad87b7ef9
## Muxer
## Demuxer
## Transcoding
## RDO
## Psychovisual quality