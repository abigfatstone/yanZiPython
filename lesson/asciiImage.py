from PIL import Image
from wordcloud import WordCloud, ImageColorGenerator
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
import jieba.analyse
import os


def isimage(fn):
    return os.path.splitext(fn)[-1] in ('.jpg', '.JPG', '.png', '.PNG')


class AsciiImage:

    def get_char(self, r, g, b, alpha=256):
        ascii_char = list(
            "$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
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
        for filename in os.listdir(os.path.dirname(dirname)):
            # 遍历所有的文件，如果是图片类型，则将文件放进列表并打印在屏幕上。
            if self.isFileType(filename, filetype):
                fileID = fileID + 1
                print('[{}]{}'.format(fileID, filename))
                fileList.append(dirname + filename)
        return fileList

    def ascii_pic(self, inUserSaid):
        # 设置resource文件夹路径
        resourceDIR = os.path.dirname(os.path.abspath(__file__)) + '/resource/'

        print("如果有新的图片需要转换，请将图片文件拷贝至文件夹" + resourceDIR)
        print("文件夹" + resourceDIR + '当前有以下图片文件：')

        # 初始化文件ID
        fileID = 0
        # 由于list的起始角标是0，为了便于理解，对于角标0放入一个空文件名，这样后面新加入的图片文件的编号（角标）可以从1开始。
        fileToAsciiList = ['']
        for filename in os.listdir(os.path.dirname(resourceDIR)):
            # 遍历所有的文件，如果是图片类型，则将文件放进列表并打印在屏幕上。
            if isimage(filename):
                fileID = fileID + 1
                print('[{}]{}'.format(fileID, filename))
                fileToAsciiList.append(resourceDIR + filename)

        # 要求输入文件编号，并转化为数字类型
        file2AsciiID = eval(input("请输入要转换的文件编号:"))
        WIDTH = 80
        HEIGHT = 40

        try:
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
            print(txt)
            return ['list_function', "AsciiImage Done", '0']
        except:
            return ['call_done', "文件编号输入错误", '0']

    def worldCloudTxt(self, inUserSaid):
        resourceDIR = os.path.dirname(os.path.abspath(__file__)) + '/resource/'
        print("如果有新的图片文件需要转换，请将图片文件拷贝至文件夹" + resourceDIR)
        print("文件夹" + resourceDIR + '当前有以下图片文件：')
        # 获取resource文件夹下的所有文件列表
        imageFileList = self.listFileType(resourceDIR, ['.jpg', '.png'])
        imageFileID = eval(input("请输入要转换的文件编号:"))

        print("如果有新的txt文件需要转换，请将txt文件拷贝至文件夹" + resourceDIR)
        print("文件夹" + resourceDIR + '当前有以下txt文件：')
        # 获取resource文件夹下的所有文件列表
        txtFileList = self.listFileType(resourceDIR, ['.txt', '.py'])
        txtFileID = eval(input("请输入要转换的文件编号:"))

        # 生成对象
        mask = np.array(Image.open(imageFileList[imageFileID]))
        # 从图片中生成颜色
        image_colors = ImageColorGenerator(mask)

        text = open(txtFileList[txtFileID]).read()
        # 中文分词
        result = jieba.analyse.extract_tags(text, topK=800, withWeight=True)
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
        homeDIR = os.path.dirname(os.path.abspath(__file__))
        fileName = os.path.split(imageFileList[imageFileID])[1]
        os.system('mkdir -p ' + homeDIR + '/../output/')
        wc.to_file(homeDIR + '/../output/out.'+fileName)
        return ['list_function', "生成的文件为："+homeDIR + '/../output/out.'+fileName, '0']


if __name__ == "__main__":
    asciiImage = AsciiImage()
    asciiImage.worldCloudTxt("ggg")
