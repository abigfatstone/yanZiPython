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
        self.functionList = '输入编号启动相应的问题\n[1]启动helloWorld\n[2]启动钟表问题'
        self.helloWorld = HelloWorld()
        self.clockAngle = ClockAngle()


    def sayHello(self):
        helloString = '姜彦孜你好，接下来将开启美妙的python程序之旅。\n'+self.functionList
        self.callbackKey = 'list_function'
        return [self.callbackKey,helloString]

    def listFunction(self):
        self.callbackKey = 'list_function'
        return [self.callbackKey,self.functionList]

    def daemonPredict(self, inUserSaid):
   
        if self.callbackKey == 'list_function':
            if inUserSaid == "1":
                aiSaid = self.helloWorld.printHelloWorld(inUserSaid)
            elif inUserSaid == '2' :
                aiSaid = self.clockAngle.getClockInput(inUserSaid)
            else:
                aiSaid = self.listFunction()

        elif self.callbackKey =='calc_clock_angle':
            aiSaid = self.clockAngle.calcClockAngle(inUserSaid)

        else:
            aiSaid = self.listFunction()

        self.callbackKey = aiSaid[0]
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


class HelloWorld():

    def printHelloWorld(self):
        print ("i love china")
        print ( 4 + 5 - (99/53) )
        print ( 4 + 5.0 - (99/53) )
        print ( 4 + 5.0 - (99/53.0) )
        print ("="*30 + '\n' + "=" + " "* 9 + "我要学编程" + " " * 9 + "=" + '\n' + "="*30)
        self.callbackKey = 'firstCall'
        return "helloWorld finished"