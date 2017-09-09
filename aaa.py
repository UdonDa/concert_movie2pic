#!/usr/bin/env python
# coding: utf-8
#
# Filename:   aaa.py
# Created at: 2017-09-09

#coding=utf-8

import cv2
import time
# 入力する動画パスを指定
cap = cv2.VideoCapture("sample.mp4")

counter = 0

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == True :
      if counter % 70 == 0:
        counter = counter + 1
        gray2 = cv2.cvtColor(frame, 1)

        # 変換するとカラー情報が落ちるので、一度ファイルにe保存して開き直す
        cv2.imwrite('./room/gray{}.png'.format(counter), gray2)
        gray = cv2.imread('./room/gray{}.png'.format(counter))

        print(frame.shape)
        print(gray2.shape)
        print(gray.shape)
        print("finish one roop")
    if ret == False and counter != 0 :
        break

cap.release()
cv2.destroyAllWindows()
