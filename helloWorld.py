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

        dTimeDetail = inTime.split(":")
        sHour = int(dTimeDetail[0])
        sMinute = int(dTimeDetail[1])
        sSecond = int(dTimeDetail[2])
        # 检查输入的数值
        if sHour < 0 or sHour>12:
            return "错误的小时格式"
        if sMinute < 0 or sMinute>60:
            return "错误的分钟格式"   
        if sSecond < 0 or sSecond>60:
            return "错误的秒针格式"    

        angleSecond = sSecond * 360.0 / 60
        angleMinute = sMinute * (360.0 / 60) + sSecond / 10.0
        angleHour = sHour * 30.0  + sMinute * (30.0 / 60) + sSecond * (30.0 /(60 * 60))
    	self.callbackKey = 'firstCall'
    	return "输入时间:{}\n时针角度:{:.4f}\n分针角度:{:.4f}\n秒针角度:{:.4f}\n".format(inTime,angleHour,angleMinute,angleSecond)

    def daemonPredict(self, inUserSaid):
        aiSaid = "Sorry,i don't know..."
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
        sysSaid = '姜彦孜最棒了!姜彦孜最美了！\n输入编号启动相应的问题\n[1]启动helloWorld\n[2]启动钟表问题'
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

