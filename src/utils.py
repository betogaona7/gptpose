from PIL import Image 
from typing import Tuple, List
import re
import ast
import numpy as np 
import cv2
import math
import logging 

def extract_data(gpt_answer:str):
    # get candidate and subset lists 
    candidate_string = re.search(r'candidate = \[(.*?)\n\]', gpt_answer, re.DOTALL).group(1)
    subset_string = re.search(r'subset = \[(.*?)\n\]', gpt_answer, re.DOTALL).group(1)
    
    # remove code comments if any
    candidate_string = re.sub(r'#.*', '', candidate_string)
    subset_string = re.sub(r'#.*', '', subset_string)
    
    # convert strings to lists
    candidate = ast.literal_eval(f'[{candidate_string.strip()}]')
    subset = ast.literal_eval(f'[{subset_string.strip()}]')
    
    return np.array(candidate), np.array(subset)


def draw_bodypose(canvas, candidate, subset):
    stickwidth = 4
    limbSeq = [[2, 3], [2, 6], [3, 4], [4, 5], [6, 7], [7, 8], [2, 9], [9, 10], \
               [10, 11], [2, 12], [12, 13], [13, 14], [2, 1], [1, 15], [15, 17], \
               [1, 16], [16, 18], [3, 17], [6, 18]]

    colors = [[255, 0, 0], [255, 85, 0], [255, 170, 0], [255, 255, 0], [170, 255, 0], [85, 255, 0], [0, 255, 0], \
              [0, 255, 85], [0, 255, 170], [0, 255, 255], [0, 170, 255], [0, 85, 255], [0, 0, 255], [85, 0, 255], \
              [170, 0, 255], [255, 0, 255], [255, 0, 170], [255, 0, 85]]
    for i in range(18):
        for n in range(len(subset)):
            index = int(subset[n][i])
            if index == -1:
                continue
            x, y = candidate[index][0:2]
            cv2.circle(canvas, (int(x), int(y)), 4, colors[i], thickness=-1)
    for i in range(17):
        for n in range(len(subset)):
            index = subset[n][np.array(limbSeq[i]) - 1]
            if -1 in index:
                continue
            cur_canvas = canvas.copy()
            Y = candidate[index.astype(int), 0]
            X = candidate[index.astype(int), 1]
            mX = np.mean(X)
            mY = np.mean(Y)
            length = ((X[0] - X[1]) ** 2 + (Y[0] - Y[1]) ** 2) ** 0.5
            angle = math.degrees(math.atan2(X[0] - X[1], Y[0] - Y[1]))
            polygon = cv2.ellipse2Poly((int(mY), int(mX)), (int(length / 2), stickwidth), int(angle), 0, 360, 1)
            cv2.fillConvexPoly(cur_canvas, polygon, colors[i])
            canvas = cv2.addWeighted(canvas, 0.4, cur_canvas, 0.6, 0)
    return canvas


def build_image(gpt_answer):
    # parse gpt answer
    candidate, subset = extract_data(gpt_answer)

    # create black canvas
    heigh, width = 512, 512
    canvas = np.zeros((heigh, width, 3), dtype=np.uint8)
    gpt_pose_image = draw_bodypose(canvas, candidate, subset)
    
    return Image.fromarray(gpt_pose_image)


def get_logger(name):
    logger = logging.getLogger(name)
    logger.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    logger.addHandler(console_handler)

    return logger