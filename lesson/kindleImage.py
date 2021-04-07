from pykeyboard import PyKeyboard
from pymouse import *
import numpy as np
import cv2
import time
import os

def snapshot_screen(page_size):
    k = PyKeyboard()
    m = PyMouse() 
    # k.tap_key('KEYTYPE_NEXT')

    p_next_page=[1414,472]
    for i in range(1,page_size):
        time.sleep(4)
        # kk.press_keys(['Command','shift','3'])
        # time.sleep(1)
        m.click(p_next_page[0],p_next_page[1])
        time.sleep(4)
        k.press_keys(['Command','shift','3'])
    
def pic_cut(source_fname,p_cut,pic_format='.png',pic_format_new='.new.jpeg'):
    convert_fname = source_fname.replace(pic_format,pic_format_new)
    box_bottom = p_cut[0][0]
    box_top = p_cut[1][0]
    box_left = p_cut[0][1]
    box_right = p_cut[1][1]
    print(source_fname)
    img = cv2.imread(source_fname).astype(np.float32)
    img = img[box_bottom:box_top, box_left:box_right]
    cv2.imwrite(convert_fname, img)

def cut_kindle_single(file_path):
    p_cut_list = [[[140,100],[1700,2770]]] # one pic
    # p_cut_list = [[[140,100],[1700,2770]],[[140,100],[1700,2770]]] # two pic
    j = 0
    for p_cut in p_cut_list:
        pic_format = '.png'
        pic_format_new = '.{}.jpeg'.format(j)
        pic_cut(file_path,p_cut,pic_format,pic_format_new)
        j = j + 1

def cut_kindle_folder(folder_name):
    for root, dirs, files in os.walk(folder_name):
        for f in files:
            file_name=file_name = "{}/{}".format(root, f)
            if f.split('.')[-1] == 'png':
                cut_kindle_single(file_name)

if __name__ == '__main__':
    cut_kindle_folder("/Users/fat/Desktop/大太阳的小房子")
