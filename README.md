# RZV2L_Yocto_Win

Yocto-LinuxのRZV2L boardを使用したWindows開発環境でPython3+OpenCV4.1を使いロボット開発を行います。

## AES-RZB-V2L-SK-G

使用するボードはAvnet Engineering Services RZBoard Development Kitです。

[Avnet Engineering Services RZBoard Development Kit](https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/rzboard-v2l/)

## WindowsでのPython3+OpenCV4.1開発環境
### 1.tera-termのインストールと設定

Windows PCにtera-termをインストールします。

[Zip DownLoad](https://osdn.net/projects/ttssh2/downloads/74780/teraterm-4.106.zip/)

[Exe Download](https://osdn.net/projects/ttssh2/downloads/74780/teraterm-4.106.exe/)

exeをダウンロードし実行するとインストールされます。

### USB シリアル 変換ケーブル TTL PL2303HXを準備します。

[USB Serial-TTL変換ケーブル](https://www.amazon.co.jp/waves-USB-%E3%82%B7%E3%83%AA%E3%82%A2%E3%83%AB-%E5%A4%89%E6%8F%9B%E3%82%B1%E3%83%BC%E3%83%96%E3%83%AB-PL2303HX/dp/B0779LL5VB/ref=sr_1_17?crid=143FA8FSAD8GK&keywords=usb+serial+%E5%A4%89%E6%8F%9B&qid=1678927636&sprefix=usb+seria%2Caps%2C194&sr=8-17)

GND:黒 5V:赤 RXD:白 TXD:緑

2.RZBoardの設定

スイッチを図の通り設定します。

3.LANの接続

LANケーブルをPCと接続します。LANを通りしてプログラムを転送します。

4.bootの書き込み

eMMCにLinuxを書き込む前にブートローダーを書き込みます。

5.avnetのyoctoイメージの書き込み

Yoctoイメージを書き込みます。

6.tera-termの起動/ifconfigでIP

IPを確認します。

6.固定IPの設定



7.コマンドプロンプトの起動

Windowsのコマンドプロンプトを起動します。

8.Windows editorでPythonプログラムの作成


9.プログラムをコピー
scp camera.py root@192.168.8.99:~root

プログラムをコピーします。

10.tera-termでプログラム起動

SSHで接続します。プログラムを起動します。
ssh root@192.168.8.99

11.バグはWindowsで編集/転送

バグ修正は8以降を繰り返します。

