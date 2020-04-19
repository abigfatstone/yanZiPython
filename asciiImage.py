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

    def get_char(self,r,g,b,alpha = 256):
        ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
        if alpha == 0:
            return ' '
        length = len(ascii_char)
        gray = int(0.2126 * r + 0.7152 * g + 0.0722 * b)

        unit = (256.0 + 1)/length
        return ascii_char[int(gray/unit)]

    def isFileType(self,filename,filetype):
        return os.path.splitext(filename.lower())[-1] in filetype

    def listFileType(self,dirname,filetype):
        #初始化文件ID
        fileID = 0
        fileList = ['']
        for filename in os.listdir(os.path.dirname(dirname)):
            #遍历所有的文件，如果是图片类型，则将文件放进列表并打印在屏幕上。
            if self.isFileType(filename,filetype):
                fileID = fileID + 1
                print('[{}]{}'.format(fileID,filename))
                fileList.append(dirname + filename)
        return fileList   

    def ascii_pic(self,inUserSaid):

        #获取程序的根目录
        cwd = os.getcwd()
        #设置resource文件夹路径
        resource_dir = os.path.dirname(cwd) +'/resource/'
        #创建resource文件夹，如果已经存在resource文件夹，该命令会被忽略
        os.system('mkdir -p ' + resource_dir)

        #获取resource文件夹下的所有文件列表
        fileList = os.listdir(os.path.dirname(resource_dir))

        # #如果是第一次运行，从resource文件夹下把初次照片拷贝到../resource下
        # if len(fileList) == 0:
        os.system("cp " + cwd +'/resource/*.* '+ resource_dir)
        #因为已经拷贝了新文件，所以重新获取文件列表
        fileList = os.listdir(os.path.dirname(resource_dir))
        
        print("如果有新的文件需要转换，请将文件拷贝至文件夹" + resource_dir )
        print("文件夹" + resource_dir +'当前有以下图片文件：')

        #初始化文件ID
        fileID = 0
        #由于list的起始角标是0，为了便于理解，对于角标0放入一个空文件名，这样后面新加入的图片文件的编号（角标）可以从1开始。
        fileToAsciiList = ['']
        for filename in os.listdir(os.path.dirname(resource_dir)):
            #遍历所有的文件，如果是图片类型，则将文件放进列表并打印在屏幕上。
            if isimage(filename):
                fileID = fileID + 1
                print('[{}]{}'.format(fileID,filename))
                fileToAsciiList.append(resource_dir + filename)

        #要求输入文件编号，并转化为数字类型
        file2AsciiID = eval(input("请输入要转换的文件编号:"))
        WIDTH = 80
        HEIGHT = 40

        try:
            #读取指定编号的文件
            im = Image.open(fileToAsciiList[file2AsciiID])
            #把图片resize
            im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

            txt = ""

            for i in range(HEIGHT):
                for j in range(WIDTH):
                    #转换为字符类型
                    txt += self.get_char(*im.getpixel((j,i)))
                txt += '\n'
            print(txt)
            return ['list_function',"AsciiImage Done",'0']
        except:
            return ['call_done',"文件编号输入错误",'0']

     

    def worldCloudTxt(self,inUserSaid):

        #获取程序的根目录
        cwd = os.getcwd()
        #设置resource文件夹路径
        resource_dir = os.path.dirname(cwd) +'/resource/'

        if not os.path.exists(resource_dir):
            #创建resource文件夹，如果已经存在resource文件夹，该命令会被忽略
            os.system('mkdir -p ' + resource_dir)
            os.system("cp " + cwd +'/resource/*.* '+ resource_dir)

        print("如果有新的图片文件需要转换，请将图片文件拷贝至文件夹" + resource_dir )
        print("文件夹" + resource_dir +'当前有以下图片文件：')
        #获取resource文件夹下的所有文件列表
        imageFileList = self.listFileType(resource_dir,['.jpg','.png'])
        imageFileID = eval(input("请输入要转换的文件编号:"))

        print("如果有新的txt文件需要转换，请将txt文件拷贝至文件夹" + resource_dir )
        print("文件夹" + resource_dir +'当前有以下txt文件：')
        #获取resource文件夹下的所有文件列表
        txtFileList = self.listFileType(resource_dir,['.txt','.py'])
        txtFileID = eval(input("请输入要转换的文件编号:"))

        # 生成对象
        mask = np.array(Image.open(imageFileList[imageFileID]))
        # 从图片中生成颜色
        image_colors = ImageColorGenerator(mask)


        text = open(txtFileList[txtFileID]).read()
        # 中文分词  
        result=jieba.analyse.extract_tags(text,topK=800,withWeight=True)
        keywords = dict()
        for i in result:
            keywords[i[0]]=i[1]

        # print(keywords)
        text = ' '.join(jieba.cut(text))

        wc = WordCloud( mask=mask, 
                        font_path="/System/Library/fonts/PingFang.ttc",
                        mode='RGBA', 
                        background_color=None,
                        max_words = 100,            # 最多词个数
                        min_font_size = 4,          # 最小字体大小
                        max_font_size = 150,        # 最大字体大小                      
                        # stopwords = stopwords,
                        random_state = 42
                        )

        # wc.generate_from_frequencies(keywords) # 从字典生成词云
        wc.generate(text) # 从字典生成词云

        wc.recolor(color_func=image_colors)
         
        # # 显示词云
        # plt.imshow(wc, interpolation='bilinear')
        # plt.axis("off")
        # plt.show()
         
        # 保存到文件
        os.system('mkdir -p ' + os.path.dirname(cwd) +'/output/')
        wc.to_file(os.path.dirname(cwd) +'/output/'+'wordCloudOut.png')
        return ['list_function',"生成的文件为："+os.path.dirname(cwd) +'/output/'+'wordCloudOut.png','0']

if __name__ == "__main__":
    asciiImage = AsciiImage()
    asciiImage.worldCloudTxt("ggg")
