# -*- coding: UTF-8 -*-
import numpy as np
import random
from itertools import permutations


class HelloWorld:

    def print_hello_world(self, inUserSaid):
        return_list = []
        return_list.append("they are autism spectrum disorder!!!")
        return_list.append(4 + 2 - (111/42))
        return_list.append(4 + 2.0 - (111/42))
        return_list.append(4 + 2.0 - (111/42.0))
        return_list.append("="*11 + '\n' + "=" + " " * 9 +
              "我要学编程" + " " * 9 + "=" + '\n' + "="*30)
        return_list.append(" " * 8+"我要学编程")
        return_list.append("我要学跳舞")
        for i in range(20, 10, -1):
            # if i ==3 :
            return_list.append("=" * i)
        return {**inUserSaid, **{'callback_key':'list_function', 'message':return_list}}
    # (递归实现)
    def Perm(self, arrs):
        # 若输入 [1,2,3]，则先取出1，将剩余的 [2,3]全排列得到 [[2,3],[3,2]]，
        # 再将 1加到全排列 [[2,3],[3,2]]上变成 [[1,2,3],[1,3,2]]
        # 同理，取出2或者3时，得到的分别是 [[2,1,3],[2,3,1]]和 [[3,1,2],[3,2,1]]
        if len(arrs) == 1:
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
        return_message = '\n'.join([' '.join('%dx%d=%2d' % (x, y, x*y)
                                  for x in range(1, y+1)) for y in range(1, 10)])
        returnKey = {'message': return_message, 'callback_key': 'list_function'}
        return {**inUserSaid, **returnKey}

    def num_to_str(self,numList):
        tmp = ''
        for num in numList:
            tmp = tmp + str(num) +' '
        return tmp.strip()

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
        listReturn = ['','1','1 1']
        for i in range(1, 10):
            list2 = []
            list2.append(list1[0])
            len1 = len(list1)
            for j in range(0, len1-1):
                list2.append(list1[j]+list1[j+1])
            list2.append(list1[-1])
            list1 = list2
            listReturn.append(self.num_to_str(list2))
        returnKey = {'message': '\n'.join(listReturn), 'callback_key': 'list_function'}
        return {**inUserSaid, **returnKey}        

    def calc_loan(self, inUserSaid):
        loan = 1000000  # 贷款金额
        annualRate = 0.04125  # 贷款年利率
        monthRate = annualRate/12  # 贷款月利率
        period = 30  # 贷款期限30年

        # 首月应还利息
        firstMonthInterest = loan*monthRate
        # 每月应还本息
        monthPayment = (loan*monthRate*(1+monthRate)**360) / \
            ((1+monthRate)**360-1)

        print("等额本息每月应还{}".format(round(monthPayment, 2)))

        loanPI = [loan*(1+monthRate)-monthPayment]
        # 每期应还利息
        loanInterest = [loan*monthRate]
        for n in range(1, period*12):
            loanPI.append((loanPI[n-1]*(1+monthRate)-monthPayment))
            loanInterest.append(round(loanPI[n-1]*monthRate, 2))

        # 每期应还本金
        loanPrincipal = [monthPayment-loanInterest[n]
                         for n in range(0, len(loanInterest))]

        for n in range(0, period*12):
            # if n % 12 == 0:
            #     print("="*20,n//12,"="*20)
            print('{:<10.2f};{:<10.2f};{:.2f}'.format(
                loanPI[n], loanInterest[n], loanPrincipal[n]))

    def calc_24(self, inUserSaid):
        stepID = inUserSaid['step_id'] + 1
        sNumberList = inUserSaid['message']
        if stepID == 1:
            returnKey = {'message':"请输入要计算24的数字，以“-”分隔，比如：1-2-3-4",'step_id': stepID}
        else:
            listNumber = sNumberList.split("-")
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

            list3 = set(list2)  # 去除重复项
            returnKey = {'message': '\n'.join(list3), 'step_id': stepID, 'callback_key': 'list_function'}
            if flag == False:
                returnKey = {'message': '无法算出', 'step_id': stepID,'callback_key': 'list_function'}
        return {**inUserSaid, **returnKey}

    def guess_num(self, inUserSaid):
        stepID = inUserSaid['step_id'] + 1
        if stepID == 1:
            randomNum = random.randint(1, 9)
            returnKey = {'message':"请在1~99之间猜一个数字",'step_id': stepID, 'randomNum': randomNum}
        elif stepID > 8:
            returnKey = {'message': '这么多次都猜不中，智商不在线啊。。。', 'callback_key': 'list_function'}
        else:
            randomNum = inUserSaid['randomNum']
            message = inUserSaid['message']
            try:
                if int(message) == randomNum:
                    returnKey = {'message': '厉害啊，居然被你猜对了！！！', 'callback_key': 'list_function'}
                elif int(message) > randomNum:
                    returnKey = {'message': '数字太大了', 'step_id': stepID}
                elif int(message) < randomNum:
                    returnKey = {'message': '数字太小了', 'step_id': stepID}
            except:
                returnKey = {'message': '输入格式错误', 'step_id': stepID - 1}

        return {**inUserSaid, **returnKey}


if __name__ == "__main__":
    helloWorld = HelloWorld()
    helloWorld.guess_num({'callbackKey':'guess_num','step_id':0})
