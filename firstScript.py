# -*- coding: UTF-8 -*-

from helloWorld import HelloWorld
from clockAngle import ClockAngle

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
        self.functionList = '输入编号启动相应的问题\n[1]启动helloWorld\n[2]启动钟表问题\n[3]计算钟表角度'
        self.helloWorld = HelloWorld()
        self.clockAngle = ClockAngle()


    def sayHello(self):
        helloString = '八二老师=八卦老师。\n'+self.functionList
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
            userSaid = raw_input(self.SENTENCES_PREFIX[1])
            if userSaid.lower() == 'exit':    
                break
            
            aiSaid = self.daemonPredict(userSaid)
            print('{}{}'.format(self.SENTENCES_PREFIX[0],aiSaid[1]))


if __name__ == "__main__":
    chatbot = Chatbot()
    chatbot.chatInteractive()
