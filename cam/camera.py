#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# 2023.05.20 version 2.0
# by T.Nishimura @AiRRC
#
#<usage>
#$ python3 camera.py
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