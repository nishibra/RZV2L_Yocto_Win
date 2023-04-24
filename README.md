# rzcv1

## AES-RZB-V2L-SK-G

Avnet Engineering Services RZBoard Development Kit

https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/rzboard-v2l/

## WindowsでのPython開発
### 1.tera-termのインストールと設定

#### Tera Term

https://osdn.net/projects/ttssh2/downloads/74780/teraterm-4.106.zip/

https://osdn.net/projects/ttssh2/downloads/74780/teraterm-4.106.exe/

exeをダウンロードし実行するとインストールされる。

#### USB シリアル 変換ケーブル TTL PL2303HX

https://www.amazon.co.jp/waves-USB-%E3%82%B7%E3%83%AA%E3%82%A2%E3%83%AB-%E5%A4%89%E6%8F%9B%E3%82%B1%E3%83%BC%E3%83%96%E3%83%AB-PL2303HX/dp/B0779LL5VB/ref=sr_1_17?crid=143FA8FSAD8GK&keywords=usb+serial+%E5%A4%89%E6%8F%9B&qid=1678927636&sprefix=usb+seria%2Caps%2C194&sr=8-17

GND:黒 5V:赤 RXD:白 TXD:緑

2.RZBoardの設定


3.LANの接続
4.bootの書き込み
5.avnetのyoctoイメージの書き込み
6.tera-termの起動/ifconfigでIP
7.WiFiの接続/ifconfigでIP
8.コマンドプロンプトの起動
9.Windows editorでPythonプログラムの作成
10.scp class_fish_calib.py root@192.168.8.108:~root
11.tera-termでプログラム起動
12.バグはWindowsで編集/転送
