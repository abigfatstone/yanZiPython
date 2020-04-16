from PIL import Image
import argparse

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
        IMG = "resource//"+input("文件路径位于~/Documents/GitHub/yanZiPython/resource：") 
        WIDTH = 80
        HEIGHT = 40
        im = Image.open(IMG)
        im = im.resize((WIDTH,HEIGHT), Image.NEAREST)

        txt = ""

        for i in range(HEIGHT):
            for j in range(WIDTH):
                txt += self.get_char(*im.getpixel((j,i)))
            txt += '\n'
        print(txt)
        return ['call_done',"drawPolygon Done",'0']