#
# Script to grayscale all images
#
import cv2
import glob
import os

def main():
  train_path = "/content/dataset/images/train/"
  test_path = "/content/dataset/images/test/"
  train_out_path = "/content/dataset/images_rgb/train"
  test_out_path = "/content/dataset/images_rgb/test"
  images_out_path = "/content/dataset/images_rgb"

  if not os.path.isdir(images_out_path) :
      os.mkdir(images_out_path)  # make sure the directory exists

  if not os.path.isdir(train_out_path) :
      os.mkdir(train_out_path)  # make sure the directory exists
  print("Grayscaling train data")
  for file_path in glob.glob(train_path + '*.png'):
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(train_out_path + '/' + os.path.basename(file_path), gray) 



  if not os.path.isdir(test_out_path) :
      os.mkdir(test_out_path)  # make sure the directory exists
  print("Grayscaling test data")
  for file_path in glob.glob(test_path + '*.png'):
    image = cv2.imread(file_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    cv2.imwrite(test_out_path + '/' + os.path.basename(file_path), gray) 

main()


