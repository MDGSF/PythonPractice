#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import os
import cv2 as cv
import numpy as np

def test():
  img = np.zeros((320, 320, 3), np.uint8) #生成一个空灰度图像
  print(img.shape) # 输出：(320, 320, 3)

  # 矩形左上角和右上角的坐标，绘制一个绿色矩形
  ptLeftTop = (60, 60)
  ptRightBottom = (260, 260)
  point_color = (0, 255, 0) # BGR
  thickness = 1
  lineType = 4
  cv.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)

  # 绘制一个红色矩形
  ptLeftTop = (120, 100)
  ptRightBottom = (200, 150)
  point_color = (0, 0, 255) # BGR
  thickness = 1
  lineType = 8
  cv.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)

  cv.namedWindow("test")
  cv.imshow('test', img)
  cv.waitKey (10000) # 显示 10000 ms 即 10s 后消失
  cv.destroyAllWindows()


def test2():
  img_path = "/home/huangjian/test/20201228172203_camera_00351770/frame_000001.jpg"
  img = cv.imread(img_path, cv.IMREAD_UNCHANGED) # 按原始颜色格式读取图片
  # img = cv.imread('/Users/wangjianjun/Desktop/Debug/pics/aaa.jpeg', cv.IMREAD_GRAYSCALE) # 按灰度图读取图片
  print(img.shape) # 输出：(240, 240, 3)

  x = 815
  y = 396
  width = 416
  height = 192

  ptLeftTop = (x, y)
  ptRightBottom = (x + width, y + height)
  point_color = (0, 255, 0) # BGR
  thickness = 1
  lineType = 4
  cv.rectangle(img, ptLeftTop, ptRightBottom, point_color, thickness, lineType)

  cv.namedWindow("image")
  cv.imshow('image', img)
  cv.waitKey(0)
  cv.destroyAllWindows()


def main():
  test2()


if __name__ == "__main__":
  main()
