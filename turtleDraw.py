# -*- coding: UTF-8 -*-
import turtle

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
        turtle.tracer(True)
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