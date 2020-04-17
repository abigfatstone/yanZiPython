from PIL import Image

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

    def ascii_pic(self,inUserSaid):

        #获取程序的根目录
        cwd = os.getcwd()
        #设置resource文件夹路径
        resource_dir = os.path.dirname(cwd) +'/resource/'
        #创建resource文件夹，如果已经存在resource文件夹，该命令会被忽略
        os.system('mkdir -p ' + resource_dir)

        #获取resource文件夹下的所有文件列表
        fileList = os.listdir(os.path.dirname(resource_dir))

        #如果是第一次运行，从resource文件夹下把初次照片拷贝到../resource下
        if len(fileList) == 0:
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
        file2AsciiID = eval(input("请选择要转换的文件编号:"))
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

