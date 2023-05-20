#!/usr/bin/env python
#! -*- coding: utf-8 -*-
#
# @author: Nishimura @ AiRRC
# 2023.05.20
import numpy as np
import cv2
import time
#
w=320
h=240
cap = cv2.VideoCapture(-1)
cap.set(3,w*2)
cap.set(4,h)
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)
class RZ_color_depth():
  def __init__(self):
    print ("Starting RZ_Stereo_Color_Detection")

    
  def find_color(self,img,ryb):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h = hsv[:, :, 0]
    s = hsv[:, :, 1]
    #v = hsv[:, :, 2]
    mask = np.zeros(h.shape, dtype=np.uint8)
    if ryb==0:
    #RED
        mask[((h>0) & (h < 13)) & (s > 128)] = 255
    elif ryb==1:
    #Yellow
        mask[((h>45) & (h < 48)) & (s > 128)] = 255
    else:
    #Blue
        mask[((h>150) & (h < 200)) & (s > 128)] = 255
    kernel = np.ones((3,3),np.uint8)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
    contours,aa= cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
#
    #cv2.imshow('mask',mask)
    rects = []
    xmax=0
    ymax=0
   # rmax=0
    for contour in contours:
        approx = cv2.convexHull(contour)
        rect = cv2.boundingRect(approx)
        rects.append(np.array(rect))
        #print (rect[0])
        #find biggest one
        nn=0
        rr=0
        for rect in rects:
            nn=nn+1
            if rr<rect[2]:
                rr=rect[2]
                xmax=int(rect[0]+rect[2]/2)
                ymax=int(rect[1]+rect[3]/2)
                #rmax=int(rect[2]/2)
    return xmax,ymax,1
#
  def cal_point_dist(self,xr,yr,xl,yl):
    #global w,h
    xd=(-xl+xr)
    yd=(-yl+yr)
    if yd<10 and yd>-10 and xd != 0:
        z=3000.0/xd
    else:
        z=0.0
    if z<0 or z>200:
        z=0.0
    x=z*((xl+xr)/2-w/2)/120
    y=-z*((yl+yr)/2-h/2)/120
    return int(x),int(y),int(z)
#
def main():
    RZ=RZ_color_depth()

    while (cap.isOpened()):
        
        timeStart=time.time()
        ret, frame = cap.read()
        
        frameL=frame[0 : h, 0: w]
        frameR=frame[0 : h, w :2*w]
        xl,yl,rflag=RZ.find_color(frameL,0)
        #print(xl,yl)
        #cv2.circle(frameL,(xl,yl),10, (0, 0, 255), thickness=-1)
        #cv2.imshow('frameL',frameL)
        if rflag==1:
            xr,yr,lflag=RZ.find_color(frameR,0)
            cv2.circle(frameL,(xl,yl),10, (0, 0, 255), thickness=-1)
            cv2.circle(frameL,(xr,yr),10, (0, 0, 255), thickness=-1)
            
            if (lflag==1) and (-xl+xr)!=0:
                x,y,z=RZ.cal_point_dist(xl,yl,xr,yr)
                timeEnd=time.time()
                fps=int(1/(timeEnd-timeStart))
                label=str(int(z))+"cm,"+str(int(fps))+"fps"
                print ("p.c.=",x,y,z,fps)
                cv2.putText(frameL,label ,(0,30), cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255,255), thickness=1)
            cv2.imshow('frameL',frameL)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print ("quit")
            break
    cap.release()
    cv2.destroyAllWindows()
#
if __name__ == "__main__":
    main()

