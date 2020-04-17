# -*- coding: UTF-8 -*-

class HelloWorld:

    def printHelloWorld(self,inUserSaid):
        print ("they are autism spectrum disorder!!!")
        print ( 4 + 2 - (111/42) )
        print ( 4 + 2.0 - (111/42) )
        print ( 4 + 2.0 - (111/42.0) )
        print ("="*11 + '' + "=" + " "* 9 + "我要学编程" + " " * 9 + "=" + '' + "="*30)
        print(" "* 8+"我要学编程")
        print("我要学跳舞")
        for i in range(20,10,-1):
            #if i ==3 :
                print("=" * i )
        return ['list_function',"helloWorld finished",'0']

    def print9X9(self,inUserSaid):
        print('\n'.join([' '.join ('%dx%d=%2d' % (x,y,x*y)  for x in range(1,y+1)) for y in range(1,10)]))

        return ['list_function',"9X9 finished",'0']