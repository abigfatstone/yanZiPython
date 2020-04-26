# -*- coding: UTF-8 -*-


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
        return ['list_function', "helloWorld finished", '0']

    def print_9X9(self, inUserSaid):
        # 这句代码值得好好理解，一句代码打印出99乘法表，后续可以考虑作为作业，自己写一段打印99乘法表的代码
        print('\n'.join([' '.join('%dx%d=%2d' % (x, y, x*y)
                                  for x in range(1, y+1)) for y in range(1, 10)]))

        return ['list_function', "9X9 finished", '0']
