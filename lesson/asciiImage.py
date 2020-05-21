# -*- coding: UTF-8 -*-

import os
from PIL import Image

import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import jieba.analyse


def isimage(fn):
    return os.path.splitext(fn)[-1] in ('.jpg', '.JPG', '.png', '.PNG')


def get_base_home():
    FILE_PATH = os.path.dirname(os.path.abspath(__file__))
    BASE_HOME = "/".join(FILE_PATH.split('/')[:-2])
    return BASE_HOME


class AsciiImage:

    def get_char(self, r, g, b, alpha=256):
        ascii_char = list(
            "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXIzcvunxrjft/()1{}[]?-_+~<>i!l;:,\"^`'. ")
        if alpha == 0:
            return ' '
        length = len(ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        unit = (256.0 + 1)/length
        return ascii_char[int(gray/unit)]

    def isFileType(self, filename, filetype):
        return os.path.splitext(filename.lower())[-1] in filetype

    def listFileType(self, dirname, filetype):
        # 初始化文件ID
        fileID = 0
        fileList = ['']
        returnList = ["文件夹" + dirname + '有以下图片文件:']
        for filename in os.listdir(os.path.dirname(dirname)):
            # 遍历所有的文件，如果是图片类型，则将文件放进列表并打印在屏幕上。
            if self.isFileType(filename, filetype):
                fileID = fileID + 1
                returnList.append('[{}]{}'.format(fileID, filename))
                fileList.append(dirname + filename)
        return fileList, returnList

    def ascii_pic(self, inUserSaid):

        WIDTH = 60
        HEIGHT = 30

        # 设置resource文件夹路径
        BASE_HOME = get_base_home()
        resourceDIR = BASE_HOME + '/resource/'

        stepID = inUserSaid['step_id'] + 1
        if stepID == 1:
            file_list, message = self.listFileType(
                resourceDIR, ['.jpg', '.png'])
            message.append("请输入要转换的文件编号:")
            returnKey = {'message': '\n'.join(message),
                         'step_id': stepID, 'file_list': file_list}
        elif stepID == 2:
            try:
                file2AsciiID = int(inUserSaid['message'])
                fileToAsciiList = inUserSaid['file_list']
                # 读取指定编号的文件
                im = Image.open(fileToAsciiList[file2AsciiID])
                # 把图片resize
                im = im.resize((WIDTH, HEIGHT), Image.NEAREST)
                txt = ""
                for i in range(HEIGHT):
                    for j in range(WIDTH):
                        # 转换为字符类型
                        txt += self.get_char(*im.getpixel((j, i)))
                    txt += '\n'
                returnKey = {'callback_key': 'list_function',
                             'step_id': stepID, 'message': txt}
            except:
                returnKey = {'callback_key': 'list_function',
                             'step_id': 0, 'message': "文件编号输入错误"}

        return {**inUserSaid, **returnKey}

    def worldCloudTxt(self, inUserSaid):

        BASE_HOME = get_base_home()
        resourceDIR = BASE_HOME + '/resource/'

        stepID = inUserSaid['step_id'] + 1
        if stepID == 1:
            file_list, message = self.listFileType(
                resourceDIR, ['.png'])
            message.append("请输入要转换的图像文件编号:")
            returnKey = {'message': '\n'.join(message),
                         'step_id': stepID, 'file_list': file_list}
        if stepID == 2:
            image_file_ID = int(inUserSaid['message'])
            image_file_List = inUserSaid['file_list']
            img_file = image_file_List[image_file_ID]
            file_list, message = self.listFileType(
                resourceDIR, ['.txt'])
            message.append("请输入要转换的文本文件编号:")
            returnKey = {'message': '\n'.join(message),
                         'step_id': stepID, 'file_list': file_list, 'img_file': img_file}

        if stepID == 3:
            txt_file_ID = int(inUserSaid['message'])
            txt_file_List = inUserSaid['file_list']
            txt_file = txt_file_List[txt_file_ID]
            img_file = inUserSaid['img_file']
            print(img_file)
            # 生成对象
            mask = np.array(Image.open(img_file))
            # 从图片中生成颜色
            image_colors = ImageColorGenerator(mask)

            text = open(txt_file).read()
            # 中文分词
            result = jieba.analyse.extract_tags(
                text, topK=800, withWeight=True)
            keywords = dict()
            for i in result:
                keywords[i[0]] = i[1]

            # print(keywords)
            text = ' '.join(jieba.cut(text))

            wc = WordCloud(mask=mask,
                           font_path="/System/Library/fonts/PingFang.ttc",
                           mode='RGBA',
                           background_color=None,
                           max_words=100,  #  最多词个数
                           min_font_size=4,  #  最小字体大小
                           max_font_size=150,  #  最大字体大小
                           # stopwords = stopwords,
                           random_state=42
                           )

            # wc.generate_from_frequencies(keywords) # 从字典生成词云
            wc.generate(text)  # 从字典生成词云

            wc.recolor(color_func=image_colors)

            # # 显示词云
            # plt.imshow(wc, interpolation='bilinear')
            # plt.axis("off")
            # plt.show()

            # 保存到文件
            OUTPUT_HOME = os.path.join(BASE_HOME, 'output')
            OUTPUT_FILENAME = 'out.' + img_file.split('/')[-1]

            OUTPUT_FILE = os.path.join(OUTPUT_HOME, OUTPUT_FILENAME)
            # print(OUTPUT_HOME,OUTPUT_FILENAME,OUTPUT_FILE)
            os.system('mkdir -p ' + OUTPUT_HOME)
            wc.to_file(OUTPUT_FILE)

            returnKey = {'message': '文件地址:'+OUTPUT_FILE,
                         'step_id': 0, 'callback_key': 'list_function'}

        return {**inUserSaid, **returnKey}


if __name__ == "__main__":
    asciiImage = AsciiImage()
    ai = asciiImage.ascii_pic({'message': "ggg", 'step_id': 0})
    print(ai['message'])
