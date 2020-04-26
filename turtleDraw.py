# -*- coding: UTF-8 -*-
import turtle
import turtle as t
import time


class TurtleDraw:

    def __init__(self):
        try:
            turtle.Terminator()
        except Exception as e:
            pass

    def turtleClose(self):
        try:
            turtle.Terminator()
        except Exception as e:
            pass

    def drawPolygon(self, inUserSaid):
        sides = eval(input("输入要绘制的边的数目（3-100）:"))
        turtle.clearscreen()
        tpen = turtle.Pen()

        turtle.bgcolor("black")

        colors = ["red", "yellow", "green", "blue", "orange", "purple"]
        for x in range(100):
            tpen.pencolor(colors[(x % sides) % 6])
            tpen.forward(x * 3 / sides + x)
            tpen.left(360 / sides + 1)
            tpen.width(x * sides / 200)
        return ['list_function', "drawPolygon Done", '0']

    def drawName(self, inUserSaid):
        turtle.clearscreen()
        tpen = turtle.Pen()
        turtle.bgcolor("black")

        my_name = turtle.textinput("输入你的姓名", "你的名字？")
        colors = ["red", "yellow", "green", "blue"]
        for x in range(60):
            tpen.pencolor(colors[x % 4])
            tpen.penup()
            tpen.forward(x * 4)
            tpen.pendown()
            tpen.write(my_name, font=("Arial", int((x + 4) / 4), "bold"))
            tpen.left(92)
        return ['list_function', "drawName Done", '0']

    def drawFlower(self, inUserSaid):
        turtle.clearscreen()
        turtle.bgcolor("black")
        turtle.color('red', 'yellow')
        turtle.begin_fill()
        while True:
            turtle.forward(200)
            turtle.left(170)
            if abs(turtle.pos()) < 1:
                break
        turtle.end_fill()
        turtle.tracer(False)
        return ['list_function', "drawFlower Done", '0']

    def drawFiveStar(self, inUserSaid):
        turtle.clearscreen()
        turtle.bgcolor("white")
        turtle.pensize(5)
        turtle.pencolor("yellow")
        turtle.fillcolor("red")

        turtle.begin_fill()
        for _ in range(5):
            turtle.forward(200)
            turtle.right(144)
        turtle.end_fill()

        turtle.penup()
        turtle.goto(-150, -120)
        turtle.color("violet")
        turtle.write("Done", font=('Arial', 40, 'normal'))
        return ['list_function', "drawFiveStar Done", '0']

    def lion(self, inUserSaid):

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
            # 下巴
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

        t.clearscreen()
        hair()
        ears(1)
        ears(-1)
        face()
        eye(1)
        eye(-1)
        mouth()
        nose()
        return ['list_function', "drawLion Done", '0']

    def drawpig(self, inUserSaid):
        t.clearscreen()
        t.pensize(4)
        t.hideturtle()
        t.colormode(255)
        t.color((255, 155, 192), "pink")
        t.setup(840, 500)
        t.speed(20)
        # 鼻子
        t.pu()
        t.goto(-100, 100)
        t.pd()
        t.seth(-30)
        t.begin_fill()
        a = 0.4
        for i in range(120):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                t.lt(3)  # 向左转3度
                t.fd(a)  # 向前走a的步长
            else:
                a = a - 0.08
                t.lt(3)
                t.fd(a)
        t.end_fill()
        t.pu()
        t.seth(90)
        t.fd(25)
        t.seth(0)
        t.fd(10)
        t.pd()
        t.pencolor(255, 155, 192)
        t.seth(10)
        t.begin_fill()
        t.circle(5)
        t.color(160, 82, 45)
        t.end_fill()
        t.pu()
        t.seth(0)
        t.fd(20)
        t.pd()
        t.pencolor(255, 155, 192)
        t.seth(10)
        t.begin_fill()
        t.circle(5)
        t.color(160, 82, 45)
        t.end_fill()
        # 头
        t.color((255, 155, 192), "pink")
        t.pu()
        t.seth(90)
        t.fd(41)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.begin_fill()
        t.seth(180)
        t.circle(300, -30)
        t.circle(100, -60)
        t.circle(80, -100)
        t.circle(150, -20)
        t.circle(60, -95)
        t.seth(161)
        t.circle(-300, 15)
        t.pu()
        t.goto(-100, 100)
        t.pd()
        t.seth(-30)
        a = 0.4
        for i in range(60):
            if 0 <= i < 30 or 60 <= i < 90:
                a = a + 0.08
                t.lt(3)  # 向左转3度
                t.fd(a)  # 向前走a的步长
            else:
                a = a - 0.08
                t.lt(3)
                t.fd(a)
        t.end_fill()
        # 耳朵
        t.color((255, 155, 192), "pink")
        t.pu()
        t.seth(90)
        t.fd(-7)
        t.seth(0)
        t.fd(70)
        t.pd()
        t.begin_fill()
        t.seth(100)
        t.circle(-50, 50)
        t.circle(-10, 120)
        t.circle(-50, 54)
        t.end_fill()
        t.pu()
        t.seth(90)
        t.fd(-12)
        t.seth(0)
        t.fd(30)
        t.pd()
        t.begin_fill()
        t.seth(100)
        t.circle(-50, 50)
        t.circle(-10, 120)
        t.circle(-50, 56)
        t.end_fill()
        # 眼睛
        t.color((255, 155, 192), "white")
        t.pu()
        t.seth(90)
        t.fd(-20)
        t.seth(0)
        t.fd(-95)
        t.pd()
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.color("black")
        t.pu()
        t.seth(90)
        t.fd(12)
        t.seth(0)
        t.fd(-3)
        t.pd()
        t.begin_fill()
        t.circle(3)
        t.end_fill()
        t.color((255, 155, 192), "white")
        t.pu()
        t.seth(90)
        t.fd(-25)
        t.seth(0)
        t.fd(40)
        t.pd()
        t.begin_fill()
        t.circle(15)
        t.end_fill()
        t.color("black")
        t.pu()
        t.seth(90)
        t.fd(12)
        t.seth(0)
        t.fd(-3)
        t.pd()
        t.begin_fill()
        t.circle(3)
        t.end_fill()
        # 腮
        t.color((255, 155, 192))
        t.pu()
        t.seth(90)
        t.fd(-95)
        t.seth(0)
        t.fd(65)
        t.pd()
        t.begin_fill()
        t.circle(30)
        t.end_fill()
        # 嘴
        t.color(239, 69, 19)
        t.pu()
        t.seth(90)
        t.fd(15)
        t.seth(0)
        t.fd(-100)
        t.pd()
        t.seth(-80)
        t.circle(30, 40)
        t.circle(40, 80)
        # 身体
        t.color("red", (255, 99, 71))
        t.pu()
        t.seth(90)
        t.fd(-20)
        t.seth(0)
        t.fd(-78)
        t.pd()
        t.begin_fill()
        t.seth(-130)
        t.circle(100, 10)
        t.circle(300, 30)
        t.seth(0)
        t.fd(230)
        t.seth(90)
        t.circle(300, 30)
        t.circle(100, 3)
        t.color((255, 155, 192), (255, 100, 100))
        t.seth(-135)
        t.circle(-80, 63)
        t.circle(-150, 24)
        t.end_fill()
        # 手
        t.color((255, 155, 192))
        t.pu()
        t.seth(90)
        t.fd(-40)
        t.seth(0)
        t.fd(-27)
        t.pd()
        t.seth(-160)
        t.circle(300, 15)
        t.pu()
        t.seth(90)
        t.fd(15)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.seth(-10)
        t.circle(-20, 90)
        t.pu()
        t.seth(90)
        t.fd(30)
        t.seth(0)
        t.fd(237)
        t.pd()
        t.seth(-20)
        t.circle(-300, 15)
        t.pu()
        t.seth(90)
        t.fd(20)
        t.seth(0)
        t.fd(0)
        t.pd()
        t.seth(-170)
        t.circle(20, 90)
        # 脚
        t.pensize(10)
        t.color((240, 128, 128))
        t.pu()
        t.seth(90)
        t.fd(-75)
        t.seth(0)
        t.fd(-180)
        t.pd()
        t.seth(-90)
        t.fd(40)
        t.seth(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)
        t.pensize(10)
        t.color((240, 128, 128))
        t.pu()
        t.seth(90)
        t.fd(40)
        t.seth(0)
        t.fd(90)
        t.pd()
        t.seth(-90)
        t.fd(40)
        t.seth(-180)
        t.color("black")
        t.pensize(15)
        t.fd(20)
        # 尾巴
        t.pensize(4)
        t.color((255, 155, 192))
        t.pu()
        t.seth(90)
        t.fd(70)
        t.seth(0)
        t.fd(95)
        t.pd()
        t.seth(0)
        t.circle(70, 20)
        t.circle(10, 330)
        t.circle(70, 30)
        return ['list_function', "drawPolygon Done", '0']
