# -*- coding: utf-8 -*-
# author：K

# 传入一个浮点型字符串和有效数字位数
def fraction_to_binary(fraction_string, significant_binary_digits):
    def print_binary(number_string, fraction_length):
        dotleft = ""

        netative = "+"
        if float(number_string) < 0:
            netative = "-"

        if "." in number_string:
            a, b = number_string.split(".")
        else:
            a = number_string
        a = int(a)
        if a < 0:
            a = -a
        result = []

        def dec2bin(number):
            if number == 1:
                result.insert(0, "1")
            elif number == 0:
                result.insert(0, "0")
            else:
                if number % 2 == 0:
                    result.insert(0, "0")
                    dec2bin(number // 2)
                else:
                    result.insert(0, "1")
                    dec2bin(number // 2)

        dec2bin(int(a))
        for i in result:
            dotleft += i
        # print(dotleft)
        if "." in number_string:

            number = float("0." + b)
            count = 0
            dotright = ""
            number = float("0." + b)
            while count < fraction_length:
                if number * 2 >= 1:
                    dotright = dotright + "1"
                    number = number * 2 - 1
                    count += 1
                else:
                    number *= 2
                    dotright = dotright + "0"
                    count += 1
        else:
            dotright = "0" * fraction_length
        temp = netative + dotleft + "." + dotright
        return temp[1:]

    answer = print_binary(fraction_string, 15)
    first_1 = answer.index("1")
    liebiao = list(answer[answer.index(".") + 1:first_1 + significant_binary_digits + 1])
    # print(liebiao)
    # 打印列表
    for i in liebiao:
        print(i, end=" ")
    print()
    # 列表打印完毕

    # 处理进位
    woshigetemp = -1
    liebiao.insert(0, "0")
    if liebiao[-1] == "1":

        while 12138:
            if liebiao[woshigetemp] == "0":

                liebiao[woshigetemp] = "1"
                break
            elif liebiao[woshigetemp] == ".":
                pass

            else:
                liebiao[woshigetemp] = "0"

            woshigetemp -= 1
    # print(liebiao[:-1])
    ###

    ###打印
    print_str = ""
    # liebiao=liebiao[:-1]
    liebiao = liebiao[:liebiao.index("1") + significant_binary_digits]
    # print(liebiao)
    liebiao.insert(1, ".")
    for i in liebiao:
        print_str += i

    print(print_str)


---------------------
作者：qq_30117591
来源：CSDN
原文：https: // blog.csdn.net / qq_30117591 / article / details / 80368246?utm_source = copy
版权声明：本文为博主原创文章，转载请附上博文链接！
