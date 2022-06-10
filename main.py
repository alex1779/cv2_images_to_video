#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 03:04:34 2020

@author: rafa
"""

import argparse
import cv2
import os
from natsort import natsorted

os.environ["IMAGEIO_FFMPEG_EXE"] = "/usr/bin/ffmpeg"


def main():

    parser = argparse.ArgumentParser(description='Save images to video')
    parser.add_argument('-i', '--input_path', type=str, default='input/',
                        help='Specify input path for images', required=True)
    parser.add_argument('-o', '--output_path', type=str, default='input/',
                        help='Specify output path video', required=True)
    parser.add_argument('-fps', '--fps', type=str, default='30',
                        help='Specify fps', required=True)
    opt = parser.parse_args()

    pathIn = opt.input_path
    pathOut = opt.output_path
    fps = int(opt.fps)
    frame_array = []
    files = natsorted(os.listdir(pathIn))
    if len(files) != 0:
        
        for i in range(len(files)):
            filename = pathIn + files[i]
            img = cv2.imread(filename)
            height, width, layers = img.shape
            size = (width, height)
            frame_array.append(img)
        out = cv2.VideoWriter(pathOut, cv2.VideoWriter_fourcc(*'DIVX'), fps, size)
        
        for i in range(len(frame_array)):
            out.write(frame_array[i])
        out.release()
    else:
        print('    ==>>>    Error. Folder input empty.')

if __name__ == '__main__':
    main()
