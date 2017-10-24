#cofing: utf-8
import os
import shutil
import cv2

def video_2_frame():
  video_file="./data/data.mp4" 
  image_dir="./image_dir/"
  image_file="img_%s.png"

  #if os.path.exits(image_dir):
    #shutil.rmtree(image_dir)

  if not os.path.exists(image_dir):
    os.makedirs(image_dir)

  i = 0
  cap = cv2.VideoCapture(video_file)
  while(cap.isOpened()):
    flag, frame = cap.read()
    if flag == False:
      break
    cv2.imwrite(image_dir + image_file % str(i).zfill(6), frame)
    print("Save: ", image_dir + image_file % str(i).zfill(6))
    i += 1

  cap.release()


if __name__ == "__main__":
  video_2_frame()
