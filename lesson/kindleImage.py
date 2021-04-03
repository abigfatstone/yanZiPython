from pykeyboard import PyKeyboard
from pymouse import *
import numpy as np
import cv2
import time

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
    img = cv2.imread(source_fname).astype(np.float32)
    img = img[box_bottom:box_top, box_left:box_right]
    cv2.imwrite(convert_fname, img)

def cut_kindle(file_path):
    p_cut_list = [[[140,100],[1700,2770]]] # one pic
    p_cut_list = [[[140,100],[1700,2770]],[[140,100],[1700,2770]]] # two pic
    j = 0
    for p_cut in p_cut_list:
        pic_format = '.png'
        pic_format_new = '.{}.jpeg'.format(j)
        pic_cut(file_path,p_cut,pic_format,pic_format_new)
        j = j + 1

if __name__ == '__main__':
    file_path = "/Users/fat/Desktop/未命名文件夹/截屏2021-04-03 下午4.27.51.png"
    cut_kindle(file_path)
