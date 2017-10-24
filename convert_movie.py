#coding=utf-8

import cv2
from numpy.random import *

# 入力する動画パスを指定
cap = cv2.VideoCapture("./data/sample.mp4")

counter = 0
dataset_counter = 0

while(cap.isOpened()):
    ret, frame = cap.read()

    if ret == True :
        counter = counter + 1

        if counter % 70 == 0 : #70フレームに一度画像処理を行う

            # グレースケールに変換
            gray2 = cv2.cvtColor(frame, 1)

            # 変換するとカラー情報が落ちるので、一度ファイルに保存して開き直す
            cv2.imwrite('./gray.png', gray2)
            gray = cv2.imread('./gray.png')

            # 切り出す位置の初期定義
            defX = 28 # 縦位置（pixel）初期値
            defY = 64 # 横位置（pixel）初期値

            # 切り出す画像の縦横幅定義
            height = 256
            width = 256

            # 縦方向ループ
            for numX in range(4):
                # 横方向ループ
                for numY in range(7):
                    dataset_counter = dataset_counter+1
                    cutX = defX + (numX * height)
                    cutY = defY + (numY * width)

                    cutImg = frame[cutX:cutX+256, cutY:cutY+256]
                    cutGray = gray[cutX:cutX+256, cutY:cutY+256]

                    # 画像の結合
                    imgAdd = cv2.hconcat([cutImg, cutGray])

                    # train:test:val = 4:1:1になるように保存ディレクトリ振り分け
                    key = rand() * 6

                if key < 4:
                    saveDir = 'train'
                elif key < 5:
                    saveDir = 'test'
                else:
                    saveDir = 'val'

                cv2.imwrite('./datasets/sample/%s/%d.png' % (saveDir, dataset_counter), imgAdd)


    if ret == False and counter != 0 :
        break

cap.release()
cv2.destroyAllWindows() 
