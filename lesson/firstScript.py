# -*- coding: UTF-8 -*-

from helloWorld import HelloWorld
from clockAngle import ClockAngle
from turtleDraw import TurtleDraw
from asciiImage import AsciiImage
import os
# from chatbotWeb import chatbotWeb  #默认不调用ai聊天


class Chatbot:

    class RunMode:
        INTERACTIVE = 'interactive'
        DAEMON = 'daemon'

    def copyResource(self):
        ########################
        # 拷贝资源文件
        ########################
        # 获取程序的根目录
        cwd = os.path.abspath(__file__)
        homeDIR = os.path.dirname(cwd)
        # 设置resource文件夹路径
        resourceDIR = homeDIR + '/../resource/'
        # 创建resource文件夹，如果已经存在resource文件夹，该命令会被忽略
        os.system('mkdir -p ' + resourceDIR)
        # 获取自带resource文件夹下的所有文件列表
        fileList = os.listdir(homeDIR + '/resource/')
        for file in fileList:
            if not os.path.exists(resourceDIR + '/' + file):
                os.system("cp " + homeDIR + '/resource/' +
                          file + ' ' + resourceDIR)

    def __init__(self):
        # Model/dataset parameters
        self.args = None
        self.copyResource()

        # 设置系统变量
        self.SENTENCES_PREFIX = ['AI: ', 'yanZi: ']
        self.sessionID = 'jiangyanzi'
        self.aiReturn = {'session_id': self.sessionID,
                         'calkback_key': 'first_call', 'step_id': 0}
        self.isDebug = False
        self.isChat = False
        self.functionList = '输入“list”，打印功能列表\n输入编号启动相应的功能\n' + \
                            '[1]启动helloWorld\n[2]计算钟表角度\n[3]计算时钟分钟夹角\n[4]打印9X9乘法表\n' + \
                            '[5]画太阳花\n[6]画五角星\n[7]画多边形\n[8]画狮子\n' + \
                            '[9]画小猪佩奇\n[10]画名字\n[11]照片转化ASCII\n[12]照片转wordCloud\n' + \
                            '[13]计算24\n[14]猜数字'

        # 初始化
        self.helloWorld = HelloWorld()
        self.clockAngle = ClockAngle()
        self.turtleDraw = TurtleDraw()
        self.asciiImage = AsciiImage()
        # if self.isChat:
        #     self.chatbotWeb = ChatbotWeb()

    def sayHello(self):
        helloString = '接下来将开始你的python奇妙之旅\n'+self.functionList
        self.aiReturn = {'session_id': self.sessionID, 'callback_key': 'list_function',
                         'step_id': 0, 'message': helloString}
        return self.aiReturn

    def listFunction(self):
        self.aiReturn = {'session_id': self.sessionID, 'callback_key': 'list_function',
                         'step_id': 0, 'message': self.functionList}
        return self.aiReturn

    def chatAsBackEnd(self, inUserInput):
        # 性能考虑，默认关闭ai聊天，返回功能列表
        # if self.isChat:
        #     aiReturn = self.chatbotWeb.chatWithBot(inUserInput)
        # else:
        #     aiReturn = self.listFunction()
        aiReturn = self.listFunction()
        return aiReturn

    def daemonPredict(self, inUserInput):
        inputMessage = inUserInput['message']
        self.aiReturn['message'] = inputMessage
        callbackKey = self.aiReturn['callback_key']        
        # 如果用户输入list，则session状态重置，打印功能列表
        if inputMessage == 'list':
            aiReturn = self.listFunction()
        # 如果用户是在等待功能列表状态，则判断启动哪个功能项
        elif callbackKey == 'list_function':
            self.aiReturn['step_id'] = 0
            if inputMessage == "1":
                aiReturn = self.helloWorld.print_hello_world(self.aiReturn)
            elif inputMessage == '2':
                aiReturn = self.clockAngle.calcClockAngle(self.aiReturn)
            elif inputMessage == '3':
                aiReturn = self.clockAngle.calcHourMinute(self.aiReturn)
            elif inputMessage == '4':
                aiReturn = self.helloWorld.print_9X9(self.aiReturn)
            elif inputMessage == '5':
                aiReturn = self.turtleDraw.drawFlower(self.aiReturn)
            elif inputMessage == '6':
                aiReturn = self.turtleDraw.drawFiveStar(self.aiReturn)
            elif inputMessage == '7':
                aiReturn = self.turtleDraw.drawPolygon(self.aiReturn)
            elif inputMessage == '8':
                aiReturn = self.turtleDraw.drawLion(self.aiReturn)
            elif inputMessage == '9':
                aiReturn = self.turtleDraw.drawpig(self.aiReturn)
            elif inputMessage == '10':
                aiReturn = self.turtleDraw.drawName(self.aiReturn)
            elif inputMessage == '11':
                aiReturn = self.asciiImage.ascii_pic(self.aiReturn)
            elif inputMessage == '12':
                aiReturn = self.asciiImage.worldCloudTxt(self.aiReturn)
            elif inputMessage == '13':
                self.aiReturn['callback_key'] = 'calc_24'
                aiReturn = self.helloWorld.calc_24(self.aiReturn)
            elif inputMessage == '14':
                self.aiReturn['callback_key'] = 'guess_num'
                aiReturn = self.helloWorld.guess_num(self.aiReturn)
            else:
                # 如果不是已知功能列表，则调用聊天程序
                aiReturn = self.chatAsBackEnd(self.aiReturn)
        elif callbackKey == 'calc_clock_angle':
            aiReturn = self.clockAngle.calcClockAngle(self.aiReturn)
        elif callbackKey == 'calc_hour_minute':
            aiReturn = self.clockAngle.calcHourMinute(self.aiReturn)
        elif callbackKey == 'calc_24':
            aiReturn = self.helloWorld.calc_24(self.aiReturn)
        elif callbackKey == 'guess_num':
            aiReturn = self.helloWorld.guess_num(self.aiReturn)
        else:
            # 如果不是已知状态，则调用聊天程序
            aiReturn = self.chatAsBackEnd(self.aiReturn)
        self.aiReturn = aiReturn
        return aiReturn

    def chatInteractive(self):
        # 初次启动，打印欢迎语
        self.sayHello()
        print('{}{}'.format(self.SENTENCES_PREFIX[0], self.aiReturn['message']))

        while True:
            inputMessage = input(self.SENTENCES_PREFIX[1])
            if inputMessage.lower() == 'exit':
                # 退出的时候关闭打开的turtle窗口，否则窗口会一直在
                self.turtleDraw.turtleClose()
                # 退出程序
                break
            user_input = {'session_id':self.sessionID,'message':inputMessage}
            aiReturn = self.daemonPredict(user_input)
            print('{}{}'.format(self.SENTENCES_PREFIX[0], aiReturn['message']))


if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chatInteractive()
