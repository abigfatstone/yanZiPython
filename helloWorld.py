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

    # (递归实现)
    def Perm(self,arrs): 
        # 若输入 [1,2,3]，则先取出1，将剩余的 [2,3]全排列得到 [[2,3],[3,2]]，
        #               再将 1加到全排列 [[2,3],[3,2]]上变成 [[1,2,3],[1,3,2]]
        # 同理，取出2或者3时，得到的分别是 [[2,1,3],[2,3,1]]和 [[3,1,2],[3,2,1]]
        if len(arrs)==1:
            return [arrs]
        result = []  # 最终的结果（即全排列的各种情况）
        for i in range(len(arrs)):  
            rest_arrs = arrs[:i]+arrs[i+1:]  # 取出arrs中的第 i个元素后剩余的元素
            rest_lists = Perm(rest_arrs)   # 剩余的元素完成全排列
            lists = []
            for term in rest_lists:
                lists.append(arrs[i:i+1]+term)  # 将取出的第 i个元素加到剩余全排列的前面
            result += lists
        return result
        
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
        list1 = [1, 1]
        list2 = []
        for i in range(1, 10):
            list2 = []
            list2.append(list1[0])
            len1 = len(list1)
            for j in range(0, len1-1):
                list2.append(list1[j]+list1[j+1])
            list2.append(list1[-1])
            list1 = list2
            print(list2)

        return ['list_function', "print yanghui delta Done", '0']

    def calc_24(self, inUserSaid):

        sStep = inUserSaid[1]
        sNumberList = inUserSaid[0]
        if sStep == '0':
            return ['calc_24', "请输入要计算24的数字，以逗号分隔，比如：1, 2, 3, 4", '1']
        else:
            listNumber = sNumberList.split(",")
            p = [c for c in permutations(listNumber, 4)]
            symbols = ["+", "-", "*", "/"]

            list2 = []  # 算出24的排列组合的列表
            ncount = 100
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
                                express = []
                                express.append("(({0} {1} {2}) {3} {4}) {5} {6}".format(
                                    one, s1, two, s2, three, s3, four))
                                express.append("({0} {1} {2}) {3} ({4} {5} {6})".format(
                                    one, s1, two, s2, three, s3, four))
                                express.append("(({0} {1} ({2} {3} {4})) {5} {6})".format(
                                    one, s1, two, s2, three, s3, four))
                                express.append("{0} {1} (({2} {3} {4}) {5} {6})".format(
                                    one, s1, two, s2, three, s3, four))
                                express.append("{0} {1} ({2} {3} ({4} {5} {6}))".format(
                                    one, s1, two, s2, three, s3, four))

                            for e in express:
                                try:
                                    if abs(eval(e)-24) < 0.01:
                                        list2.append(e+" = 24")
                                        ncount = ncount+2
                                        flag = True
                                except ZeroDivisionError:
                                    pass
            print(ncount)
            list3 = set(list2)  # 去除重复项
            for c in list3:
                print(c)
            if flag == False:
                print("无法算出")
        return ['list_function', "calc 24 Done", '0']

def 

if __name__ == "__main__":
    helloWorld = HelloWorld()
    helloWorld.print_yanghui_deleta(["1,2,3,5", '1'])
