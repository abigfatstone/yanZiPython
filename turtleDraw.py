# -*- coding: UTF-8 -*-
import turtle
import time
import turtle as t

class TurtleDraw:

    def drawPolygon(self,inUserSaid):
        t = turtle.Pen()
        turtle.bgcolor("black")
        sides = eval(input("输入要绘制的边的数目（2-6）！"))
        colors = ["red", "yellow", "green", "blue", "orange", "purple"]
        for x in range(100):
            t.pencolor(colors[x % sides])
            t.forward(x * 3 / sides + x)
            t.left(360 / sides + 1)
            t.width(x * sides / 200)
        return ['call_done',"drawPolygon Done",'0']


    def drawName(self,inUserSaid):
        t = turtle.Pen()
        turtle.bgcolor("black")

        my_name = turtle.textinput("输入你的姓名", "你的名字？")
        colors = ["red", "yellow", "purple", "blue"]
        for x in range(100):
            t.pencolor(colors[x % 4])
            t.penup()
            t.forward(x * 4)
            t.pendown()
            t.write(my_name, font=("Arial", int((x + 4) / 4), "bold"))
            t.left(92)
        return ['call_done',"drawName Done",'0']

    def drawFlower(self,inUserSaid):
        turtle.color('red','yellow')
        turtle.begin_fill()
        while True:
            turtle.forward(200)
            turtle.left(170)
            if abs(turtle.pos()) <1:
                break
        turtle.end_fill()
        turtle.tracer(False)
        return ['call_done',"drawName Done",'0']


    def drawFiveStar(self,inUserSaid):
        turtle.pensize(5)
        turtle.pencolor("yellow")
        turtle.fillcolor("red")
         
        turtle.begin_fill()
        for _ in range(5):
          turtle.forward(200)
          turtle.right(144)
        turtle.end_fill()
        time.sleep(2)
         
        turtle.penup()
        turtle.goto(-150,-120)
        turtle.color("violet")
        turtle.write("Done", font=('Arial', 40, 'normal'))
         
        turtle.mainloop()

    

    def hair():    # 画头发
        t.penup()
        t.goto(-50, 150)
        t.pendown()
        t.fillcolor('#a2774d')
        t.begin_fill()
        for j in range(10):                   # 重复执行10次
            t.setheading(60 - (j * 36))       # 每次调整初始角度
            t.circle(-50, 120)                # 画120度的弧
        t.end_fill()

    def face():    # 画脸
        t.penup()
        t.goto(0, 100)
        t.pendown()
        t.fillcolor('#f2ae20')
        t.begin_fill()
        t.setheading(180)
        t.circle(85)
        t.end_fill()
        #下巴
        t.circle(85, 120)
        t.fillcolor('white')
        t.begin_fill()
        t.circle(85, 120)
        t.setheading(135)
        t.circle(100, 95)
        t.end_fill()
        
    def ears(dir):    # 画眼睛，dir用来设置方向，左右眼对称
        t.penup()
        t.goto((0-dir)*30, 90)
        t.setheading(90)
        t.pendown()
        t.fillcolor('#f2ae20')
        t.begin_fill()
        t.circle(dir*30)
        t.end_fill()
        
        t.penup()
        t.goto((0-dir)*40, 85)
        t.setheading(90)
        t.pendown()
        t.fillcolor('white')
        t.begin_fill()
        t.circle(dir*17)
        t.end_fill()
        
    def nose():    # 画鼻子
        t.penup()
        t.goto(20, 0)
        t.setheading(90)
        t.pendown()
        t.fillcolor('#a2774d')
        t.begin_fill()
        t.circle(20)
        t.end_fill()
        
    def eye(dir):    # 画耳朵，dir用来设置方向，左右耳对称
        t.penup()
        t.goto((0-dir)*30, 20)
        t.setheading(0)
        t.pendown()
        t.fillcolor('black')
        t.begin_fill()
        t.circle(10)
        t.end_fill()

    def mouth():    # 画嘴巴
        t.penup()
        t.goto(0, 0)
        t.setheading(-90)
        t.pendown()
        t.forward(50)
        t.setheading(0)
        t.circle(80, 30)
        t.penup()
        t.goto(0, -50)
        t.setheading(180)
        t.pendown()
        t.circle(-80, 30)   
        
    def lion(self,inUserSaid):
        hair()
        ears(1)
        ears(-1)
        face()
        eye(1)
        eye(-1)
        mouth()
        nose()
        t.done()
        return ['call_done',"drawPolygon Done",'0']

                　