# -*- coding: UTF-8 -*-
import numpy as np
from itertools import permutations

class HelloWorld:

    def print_hello_world(self, inUserSaid):
        print("they are autism spectrum disorder!!!")
        print(4 + 2 - (111/42))
        print(4 + 2.0 - (111/42))
        print(4 + 2.0 - (111/42.0))
        print("="*11 + '\n' + "=" + " " * 9 +
              "我要学编程" + " " * 9 + "=" + '\n' + "="*30)
        print(" " * 8+"我要学编程")
        print("我要学跳舞")
        for i in range(20, 10, -1):
            # if i ==3 :
            print("=" * i)
        return ['list_function', "helloWorld Done", '0']

    def print_9X9(self, inUserSaid):
        # 这句代码值得好好理解，一句代码打印出99乘法表，后续可以考虑作为作业，自己写一段打印99乘法表的代码
        print('\n'.join([' '.join('%dx%d=%2d' % (x, y, x*y)
                                  for x in range(1, y+1)) for y in range(1, 10)]))

        return ['list_function', "9X9 Done", '0']

    def print_yanghui_deleta(self, inUserSaid):
        # 打印杨辉三角
        # 1
        # 1 1
        # 1 2 1
        # 1 3 3 1
        # 1 4 6 4 1
        # 1 5 10 10 5 1

        return ['list_function', "print yanghui delta Done", '0']

    def calc_24(self, inUserSaid):

        sStep = inUserSaid[1]
        sNumberList = inUserSaid[0]
        if sStep == '0':
            return ['calc_24', "请输入要计算24的数字，以逗号分隔，比如：1, 2, 3, 4",'1']
        else:
            listNumber = sNumberList.split(",")
            p = [c for c in permutations(listNumber, 4)]
            symbols = ["+", "-", "*", "/"]

            list2 = []  # 算出24的排列组合的列表

            flag = False
            for n in p:
                one, two, three, four = n
                for s1 in symbols:
                    for s2 in symbols:
                        for s3 in symbols:
                            if s1+s2+s3 == "+++" or s1+s2+s3 == "***":
                                express = ["{0} {1} {2} {3} {4} {5} {6}".format(
                                    one, s1, two, s2, three, s3, four)]  # 全加或者乘时，括号已经没有意义。
                            else:
                                express = ["(({0} {1} {2}) {3} {4}) {5} {6}".format(one, s1, two, s2, three, s3, four),
                                           "({0} {1} {2}) {3} ({4} {5} {6})".format(
                                    one, s1, two, s2, three, s3, four),
                                    "(({0} {1} ({2} {3} {4})) {5} {6})".format(
                                    one, s1, two, s2, three, s3, four),
                                    "{0} {1} (({2} {3} {4}) {5} {6})".format(
                                    one, s1, two, s2, three, s3, four),
                                    "{0} {1} ({2} {3} ({4} {5} {6}))".format(one, s1, two, s2, three, s3, four)]

                            for e in express:
                                try:
                                    if abs(eval(e)-24) < 0.01:
                                        list2.append(e+" = 24")
                                        flag = True
                                except ZeroDivisionError:
                                    pass

            list3 = set(list2)  # 去除重复项
            for c in list3:
                print(c)
            if flag == False:
                print("无法算出")
        return ['list_function', "calc 24 Done", '0']


if __name__ == "__main__":
    helloWorld = HelloWorld()
    helloWorld.calc_24(["5,5,10,10", '1'])
