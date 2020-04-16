# -*- coding: UTF-8 -*-

from helloWorld import HelloWorld
from clockAngle import ClockAngle
from turtleDraw import TurtleDraw

class Chatbot:

    class RunMode:
        INTERACTIVE = 'interactive'
        DAEMON ='daemon'

    def __init__(self):
        # Model/dataset parameters
        self.args = None
        self.SENTENCES_PREFIX = ['AI: ', 'yanZi: ']
        self.callbackKey = 'first_call'
        self.stepID = '0'
        self.is_debug = '0'
        self.functionList = '输入编号启动相应的问题\n[1]启动helloWorld\n[2]启动钟表问题\n[3]计算钟表角度\n[4]打印9X9乘法表\n[5]绘制多边形\n' +\
                            '[6]画五角星\n[7]画多边形\n[8]画名字形状'
        self.helloWorld = HelloWorld()
        self.clockAngle = ClockAngle()
        self.turtleDraw = TurtleDraw()


    def sayHello(self):
        helloString = '姜彦孜你好，开始你的python之旅\n'+self.functionList
        self.callbackKey = 'list_function'
        self.stepID ='0'
        return [self.callbackKey,helloString,self.stepID]

    def listFunction(self):
        self.callbackKey = 'list_function'
        self.stepID ='0'
        return [self.callbackKey,self.functionList,self.stepID]

    def daemonPredict(self, inUserSaid):

        if self.is_debug == '1':
            print([inUserSaid,self.callbackKey,self.stepID,"start daemonPredict"])

        if self.callbackKey == 'list_function':
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
            else:
                aiSaid = self.listFunction()

        elif self.callbackKey =='calc_clock_angle':
            aiSaid = self.clockAngle.calcClockAngle([inUserSaid,self.stepID])

        elif self.callbackKey =='calc_hour_minute':
            aiSaid = self.clockAngle.calcHourMinute([inUserSaid,self.stepID])
            
        else:
            aiSaid = self.listFunction()

        self.callbackKey = aiSaid[0]
        self.stepID = aiSaid[2]

        return aiSaid


    def chatInteractive(self):
        aiSaid = self.sayHello()
        print('{}{}'.format(self.SENTENCES_PREFIX[0],aiSaid[1]))
        
        while True:
            userSaid = input(self.SENTENCES_PREFIX[1])
            if userSaid.lower() == 'exit':    
                break
            
            aiSaid = self.daemonPredict(userSaid)
            print('{}{}'.format(self.SENTENCES_PREFIX[0],aiSaid[1]))


if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chatInteractive()
