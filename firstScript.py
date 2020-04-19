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
        DAEMON ='daemon'
    def copyResource(self):
        ########################
        #拷贝资源文件
        ########################
        #获取程序的根目录
        cwd = os.path.abspath(__file__)
        homeDIR = os.path.dirname(cwd)
        #设置resource文件夹路径
        resourceDIR = homeDIR +'/../resource/'
        #创建resource文件夹，如果已经存在resource文件夹，该命令会被忽略
        os.system('mkdir -p ' + resourceDIR)
        #获取自带resource文件夹下的所有文件列表
        fileList = os.listdir(homeDIR +'/resource/')
        for file in fileList:
            if not os.path.exists(resourceDIR + '/' + file):
                os.system("cp " + homeDIR +'/resource/'+ file +' ' + resourceDIR)
                
    def __init__(self):
        # Model/dataset parameters
        self.args = None
        self.copyResource()

        #设置系统变量
        self.SENTENCES_PREFIX = ['AI: ', 'yanZi: ']
        self.callbackKey = 'first_call'
        self.stepID = '0'
        self.isDebug = False
        self.isChat = False
        self.functionList = '输入“list”，打印功能列表\n输入编号启动相应的问题\n' + \
                            '[1]启动helloWorld\n[2]计算钟表角度\n[3]计算时钟分钟夹角\n[4]打印9X9乘法表\n' + \
                            '[5]画太阳花\n[6]画五角星\n[7]画多边形\n[8]画狮子\n' + \
                            '[9]画小猪佩奇\n[10]画名字\n[11]照片转化ASCII\n[12]照片转wordCloud'

        #初始化
        self.helloWorld = HelloWorld()
        self.clockAngle = ClockAngle()
        self.turtleDraw = TurtleDraw()
        self.asciiImage = AsciiImage()
        # if self.isChat:
        #     self.chatbotWeb = ChatbotWeb()


    def sayHello(self):
        helloString = '姜彦孜你好，接下来将开始你的python奇妙之旅\n'+self.functionList
        self.callbackKey = 'list_function'
        self.stepID ='0'
        return [self.callbackKey,helloString,self.stepID]

    def listFunction(self):
        self.callbackKey = 'list_function'
        self.stepID ='0'
        return [self.callbackKey,self.functionList,self.stepID]

    def chatAsBackEnd(self,inUserInput):
        #性能考虑，默认关闭ai聊天，返回功能列表
        # if self.isChat:
        #     aiSaid = self.chatbotWeb.chatWithBot(inUserInput)
        # else:
        #     aiSaid = self.listFunction()
        aiSaid = self.listFunction()    
        return aiSaid

    def daemonPredict(self, inUserSaid):

        if self.isDebug:
            print([inUserSaid,self.callbackKey,self.stepID,"start daemonPredict"])
        #如果用户输入list，则session状态重置，打印功能列表
        if inUserSaid == 'list':
            aiSaid = self.listFunction()
        #如果用户是在等待功能列表状态，则判断启动哪个功能项    
        elif self.callbackKey == 'list_function':
            if inUserSaid == "1":
                aiSaid = self.helloWorld.printHelloWorld([inUserSaid,'0'])
            elif inUserSaid == '2' :
                aiSaid = self.clockAngle.calcClockAngle([inUserSaid,'0'])
            elif inUserSaid == '3' :
                aiSaid = self.clockAngle.calcHourMinute([inUserSaid,'0'])    
            elif inUserSaid == '4' :
                aiSaid = self.helloWorld.print9X9([inUserSaid,'0'])  
            elif inUserSaid == '5' :
                aiSaid = self.turtleDraw.drawFlower([inUserSaid,'0'])  
            elif inUserSaid == '6' :
                aiSaid = self.turtleDraw.drawFiveStar([inUserSaid,'0'])  
            elif inUserSaid == '7' :
                aiSaid = self.turtleDraw.drawPolygon([inUserSaid,'0'])      
            elif inUserSaid == '8' :
                aiSaid = self.turtleDraw.lion([inUserSaid,'0']) 
            elif inUserSaid == '9' :
                aiSaid = self.turtleDraw.drawpig([inUserSaid,'0']) 
            elif inUserSaid == '10' :
                aiSaid = self.turtleDraw.drawName([inUserSaid,'0'])     
            elif inUserSaid == '11' :
                aiSaid = self.asciiImage.ascii_pic([inUserSaid,'0'])    
            elif inUserSaid == '12' :
                aiSaid = self.asciiImage.worldCloudTxt([inUserSaid,'0'])                                                          
            else:
                #如果不是已知功能列表，则调用聊天程序
                aiSaid = self.chatAsBackEnd([inUserSaid,'0'])
        elif self.callbackKey =='calc_clock_angle':
            aiSaid = self.clockAngle.calcClockAngle([inUserSaid,self.stepID])
        elif self.callbackKey =='calc_hour_minute':
            aiSaid = self.clockAngle.calcHourMinute([inUserSaid,self.stepID])
        else:
            #如果不是已知状态，则调用聊天程序
            aiSaid = self.chatAsBackEnd([inUserSaid,'0'])

        self.callbackKey = aiSaid[0]
        self.stepID = aiSaid[2]

        return aiSaid


    def chatInteractive(self):
        #初次启动，打印欢迎语
        aiSaid = self.sayHello()
        print('{}{}'.format(self.SENTENCES_PREFIX[0],aiSaid[1]))
        
        while True:
            userSaid = input(self.SENTENCES_PREFIX[1])
            if userSaid.lower() == 'exit':   
                #退出的时候关闭打开的turtle窗口，否则窗口会一直在
                self.turtleDraw.turtleClose()
                #退出程序
                break
            
            aiSaid = self.daemonPredict(userSaid)
            print('{}{}'.format(self.SENTENCES_PREFIX[0],aiSaid[1]))


if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chatInteractive()
