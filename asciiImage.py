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

        IMG = "resource//acd.jpg"
        cwd = os.getcwd()
        resource_dir = os.path.dirname(cwd) +'/resource/'
        os.system('mkdir -p ' + resource_dir)
        fileList = os.listdir(os.path.dirname(resource_dir))
        if len(fileList) == 0:
            os.system("cp " + cwd +'/resource/*.* '+ resource_dir)
            fileList = os.listdir(os.path.dirname(resource_dir))
        # IMG = "resource//acd.jpg"+input("文件路径位于~/Documents/GitHub/yanZiPython/resource：") 
        
        print("如果有新的文件需要转换，请将文件拷贝至文件夹" + resource_dir )
        print("文件夹" + resource_dir +'当前有以下图片文件：')
        fileID = 0
        fileToAsciiList = []
        for filename in os.listdir(os.path.dirname(resource_dir)):
            if isimage(filename):
                print('[{}]{}'.format(fileID,filename))
                fileToAsciiList.append(resource_dir + filename)
                fileID = fileID + 1

        file2AsciiID = eval(input("请选择要转换的文件编号:"))
        WIDTH = 80
        HEIGHT = 40

        try:
            im = Image.open(fileToAsciiList[file2AsciiID])
            im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

            txt = ""

            for i in range(HEIGHT):
                for j in range(WIDTH):
                    txt += self.get_char(*im.getpixel((j,i)))
                txt += '\n'
            print(txt)
            return ['list_function',"AsciiImage Done",'0']
        except:
            return ['call_done',"文件编号输入错误",'0']

