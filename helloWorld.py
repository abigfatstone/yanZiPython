# -*- coding: UTF-8 -*-


class Chatbot:

    class RunMode:
        INTERACTIVE = 'interactive'
        DAEMON ='daemon'

    def __init__(self):
        # Model/dataset parameters
        self.args = None
        self.SENTENCES_PREFIX = ['AI: ', 'yanZi: ']
        self.callbackKey = 'firstCall'

    def printHelloWorld(self):
        print ("i love china")
        print ( 4 + 5 - (99/53) )
        print ( 4 + 5.0 - (99/53) )
        print ( 4 + 5.0 - (99/53.0) )
        print ("="*30 + '\n' + "=" + " "* 9 + "我要学编程" + " " * 9 + "=" + '\n' + "="*30)
        self.callbackKey = 'firstCall'
        return "helloWorld finished"

    def timeRun(self,inTime):

    	self.callbackKey = 'firstCall'
    	return "debug time_run:{}".format(inTime)

    def daemonPredict(self, inUserSaid):
        aiSaid = "Sorry,i don't know..."
        print(self.callbackKey)
        if self.callbackKey == 'firstCall':
            if inUserSaid == "1":
                aiSaid = self.printHelloWorld()
            elif inUserSaid == '2' :
   	            aiSaid = "请以下格式输入要计算的时间HH:MI:SS,例如04:35:00"
   	            self.callbackKey = 'time_run'

    	elif self.callbackKey =='time_run':
    		aiSaid = self.timeRun(inUserSaid)

        return aiSaid


    def chatInteractive(self):
        sysSaid = '输入编号启动相应的问题\n'+ '[1]启动helloWorld\n[2]启动钟表问题'
        print('{}{}'.format(self.SENTENCES_PREFIX[0],sysSaid))

        while True:
            userSaid = raw_input(self.SENTENCES_PREFIX[1])
            if userSaid.lower() == 'exit':    
                break
            
            sysSaid = self.daemonPredict(userSaid)
            print('{}{}'.format(self.SENTENCES_PREFIX[0],sysSaid))


if __name__ == "__main__":
	chatbot = Chatbot()
	chatbot.chatInteractive()

