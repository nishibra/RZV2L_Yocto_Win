# RZV2L_Yocto_Win

Yocto-LinuxのRZV2L boardを使用したWindows開発環境でPython3+OpenCV4.1を使いロボット開発を行います。


### AES-RZB-V2L-SK-G

使用するボードはAvnet Engineering Services RZBoard Development Kitです。

[Avnet Engineering Services RZBoard Development Kit](https://www.avnet.com/wps/portal/us/products/avnet-boards/avnet-board-families/rzboard-v2l/)

![RZ-Board](/pics/rzboard.jpg)


## WindowsでのPython3+OpenCV4.1開発環境
### 1.tera-termのインストールと設定

Windows PCにtera-termをインストールします。

[Zip DownLoad](https://osdn.net/projects/ttssh2/downloads/74780/teraterm-4.106.zip/)

[Exe Download](https://osdn.net/projects/ttssh2/downloads/74780/teraterm-4.106.exe/)

exeをダウンロードし実行するとインストールされます。

### 2.USB シリアル 変換ケーブル TTL PL2303HXを準備します。

[USB Serial-TTL変換ケーブル](https://www.amazon.co.jp/waves-USB-%E3%82%B7%E3%83%AA%E3%82%A2%E3%83%AB-%E5%A4%89%E6%8F%9B%E3%82%B1%E3%83%BC%E3%83%96%E3%83%AB-PL2303HX/dp/B0779LL5VB/ref=sr_1_17?crid=143FA8FSAD8GK&keywords=usb+serial+%E5%A4%89%E6%8F%9B&qid=1678927636&sprefix=usb+seria%2Caps%2C194&sr=8-17)
```
GND:黒 5V:赤 RXD:白 TXD:緑
```
### 3.RZBoardの設定

![SW_RZ-Board](/pics/sw_set.jpg)

スイッチを図の通り設定します。

#### 4.LANの接続(購入時に書き込まれているので省略可)

LANケーブルをPCと接続します。LANを通してプログラムを転送します。

### 5.bootの書き込み(購入時に書き込まれているので省略可)

eMMCにLinuxを書き込む前にブートローダーを書き込みます。

### 6.yoctoイメージの書き込み

以下よりyocto imageをdownloadします。

[yocto image ver3.1.17](http://www.arrc.jp/auto/avnet-core-image-rzboard-20230509230035.rootfs.wic)

YoctoイメージをWin32DiskImagerを使ってSDカードに書き込み、RZ-Boardに挿します。

### 7.tera-termの起動/ifconfigでIP

LANケーブルをWindows PCと同じルーターに接続します。

以下を入力しIPアドレスを確認します。
```
$ ifconfig
```

### 8.固定IPの設定

有線LanのStatic IP(ここでは192.168.8.99とします。)をセットします。

まずLANの設定ファイルを作成します。
```
# nano /etc/systemd/network/01-eth0.network
```
以下ファイルの内容です。
```
#01-eth0.network
[Match]
Name=eth0
[Network]
Address=192.168.8.99/24
Gateway=192.168.8.1
DNS=114.114.114.114
DNS=223.6.6.6
```
保存して終了し、再起動するとIPが変更されます。
ifconfigで確認できます。


### 9.Windows editorでPython3プログラムの作成

エディターでPython3のプログラムを作成します。
rz_workなどと作業ディレクトリーを作成しプログラムを保存します。

```
#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
import cv2
#
def main():
  print ('start camera')
  cap = cv2.VideoCapture(-1)
  cap.set(3,640)
  cap.set(4,240)
  cap.set(5,30)
  cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
  
  while (cap.isOpened()):
    ret, data = cap.read()
    frameHeight = data.shape[0]
    frameWidth = data.shape[1]
    print(frameWidth,frameHeight)
    cv2.imshow('image',data)
    if cv2.waitKey(1) & 0xFF == ord('q'):
      print ("quit")
      break
  cap.release()
  cv2.destroyAllWindows()
#
if __name__ == "__main__":
    main()
```

### 10.コマンドプロンプトでプログラムをRZボードに転送

Windowsのコマンドプロンプトを起動します。(windowsシステムツールの中にコマンドプロンプトがあります。)

scpコマンドで作成したcamera.pyをRZボードに転送します。

```
$ scp camera.py root@192.168.8.99:~root
# ls
```
コピーされているかを確認します。

### 11.tera-termでプログラムを実行

以下でプログラムを実行します。
```
# python3 camera.py
```
RZ-ボードに接続したHDMI Displayにカメラ画像が表示されます。

### 12.コマンドプロンプトからSSHで接続

SSHで接続します。
```
$ ssh root@192.168.8.99
```
SSHで接続することでデバック用シリアルケーブルは不要です。ネットでの開発が可能となります。

### 13.デバッグはWindowsで編集/転送

バグ修正は9以降を繰り返します。

