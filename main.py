# This is a sample Python script.

import calendar
import cmath
import math
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random
import sys
import time

import numpy as numpy

import module1


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def sys_wr(str):
    x = 'runoob'
    sys.stdout.write(x + '\n')
    print(f'Hi, {str}')


def if_ex(i):
    if i < 1:
        print('小于1')
    elif i < 2:
        print('小于2')
    else:
        print('大于2')
    if 1: print("同一行的if语句")


def say_love(word):
    if word == "I love you":
        print("I love you too.")
    elif word == "I don't love you":
        print("I will be the one.")
    else:
        print("please say 'I love you'")


def list_split():
    s = 'qwertyuiop'
    sys.stdout.write('截取1到5之间的字符串' + s[1:5] + "\n")


def count_m():
    addc = 2 + 2
    dec = 2 - 2
    multi = 2 * 2  # 乘法
    multi_s = 2 ** 4  # 幂次方，2的4次幂
    delv = 2 / 2  # 除法
    delv_i = 2 % 3  # 取模，除法余数
    delv_f = 2.0 / 4  # float类型相除，值可为小数
    delv_r = 4 // 3  # 向下取整
    print("+:" + str(addc) + ";-:" + str(dec) + ";x:" + str(multi) + ";xx:" + str(multi_s) + ";/:" + str(
        delv) + ";%:" + str(delv_i) + ";/f:" + str(delv_f) + ";/r:" + str(delv_r))


def for_ex():
    a = 1
    b = 0
    while a < 5:
        print(str(a) + "小于5\n")
        a += 1
    fruits = ['apple', 'orange', 'banana', 'pear']
    for i in fruits:
        print("for循环水果" + i)
    for index in range(len(fruits)):
        print('for循环下标第' + str(index) + '个水果是:' + fruits[index])
    # for...else
    for n in range(10, 15):  # 这是右开区间
        for m in range(2, n):
            if n % m == 0:
                j = n / m
                print('%d 等于 %d * %d' % (n, m, j))
                break
        else:
            print("%d是一个质数" % n)
    for x in range(5):
        if x <= 2:
            print("%d 不大于2" % x)
        else:
            continue
    for y in range(1, 5):
        if y % 2 == 0 and y != 2:
            print("1-5 内第一个不等于2且被2整除的数%d" % y)
            break


def draw_t():
    rows = 10
    i = j = k = 1
    for i in range(0, rows):
        for k in range(0, rows):
            if i != 0 and i != rows - 1:
                if k == 0 or k == rows - 1:
                    # 由于视觉效果看起来更像正方形，所以这里*两侧加了空格，增大距离
                    print(" * "),  # 注意这里的","，一定不能省略，可以起到不换行的作用
                else:
                    print("   "),  # 该处有三个空格
            else:
                print(" * "),  # 这里*两侧加了空格
            k += 1
        i += 1
        print("\n")


def function():
    pass  # 占位符，没有想好的空函数或者方法可以使用


def del_fun():
    a = 0
    del a  # 删除变量


def var_type():
    int_v = 1
    long_v = 51924361  # 3.0以上版本不支持写l表示
    float_v = 0.0
    complex_v = 2 + 3j
    c_2 = complex_v ** 2
    print('复数的真实' + str(complex_v.real) + '虚数部分' + str(complex_v.imag) + '复数的乘积' + str(c_2))


def look_math():
    dir(math)
    dir(cmath)
    print('-1的虚数根为' + str(cmath.sqrt(-1)))
    print('1的sin虚数为' + str(cmath.sin(1)))
    list1 = [1, 2, 3, 4, 5]
    print('最大%d' % max(list1) + '最小%d' % min(list1))
    print('10为底的100的对数%d' % math.log10(100))
    print('10.03的整数和小数部分' + str(math.modf(10.03)))
    print('3的2次方%d' % math.pow(3, 2))
    print('9的平方根%d' % math.sqrt(9))
    print('3.14158四舍五入到小数点后两位%f' % round(3.14158, 2))


def random_fun():
    # random函数 随机数
    print('序列的随机数%d' % random.choice(range(10)))
    print('指定5-10随机数%d' % random.randrange(3, 10, 2))
    print('随机0-1实数%f' % random.random())
    print('随机多维数组' + str(numpy.random.rand(3, 4, 5)))  # 三维、四组、每组5个值
    print('多维数组遵循N(0,1)正态分布' + str(numpy.random.randn(3, 2, 2)))
    ls = [1, 3, 5, 7, 9]
    random.shuffle(ls)
    print('序列元素随机不排序'+str(ls))
    print('随机生成0-100内实数%f' % random.uniform(0, 100))
    # 三角函数
    print('sin90度的值%f和sin30度值' % math.sin(math.pi/2), math.sin(math.pi/6))
    print('sin90度的值%f和sin30度值' % math.sin(math.pi / 6), math.sin(math.pi / 6)) # %的位置不同，值不同
    # 弧度转角度
    print('弧度-》角度%f' % math.degrees(math.pi/2))
    print('角度-》弧度%f' % math.radians(90.0))


def str_fun():
    # 响铃
    print('\a')
    # 原始字符串
    print(r'\a')
    print('格式化字符串%s的年龄%d' % ('zs', 10))
    print(u'使用unicode编码Hello\u0020World !')
    # 三引号字符
    print('''
<HTML><HEAD><TITLE>
Friends CGI Demo</TITLE></HEAD>
<BODY><H3>ERROR</H3>
<B>%s</B><P>
<FORM><INPUT TYPE=button VALUE=Back
ONCLICK="window.history.back()"></FORM>
</BODY></HTML>
''')

def timeFm():
    t = time.time()
    localtime = time.localtime(time.time())
    fmT = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    print(fmT)
    cal = calendar.month(2016, 1)
    print("以下输出2016年1月份的日历:")
    print(cal)


def lamdaFun():
    sumL = lambda arg1, arg2: arg1+arg2
    count = sumL(1, 2)
    print('lambda表达:%d' % count)


def argsT(arg1, *args):
    print("参数1："+arg1)
    for a in args:
        print(a)


def argsV():
    a, b = 2, 3
    print("%d 参数b：%d" % (a, b))


def funX(x):
    def funY(y):
        return x * y
    return funY(8)


def multiF(x, y):
    return x * y


def funUS(func, x, y):
    # 函数名作为参数调用函数
    print("函数名调用 %d" % (func(x, y)+func(x, y)))


def dirF():
    list = dir(math)
    print(list)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    sys_wr('sys')
    if_ex(-1)
    list_split()
    say_love("I love you")
    count_m()
    for_ex()
    var_type()
    look_math()
    random_fun()
    str_fun()
    lamdaFun()
    argsT('1', '2', '3')
    argsV()
    print("双重fun: %d" % funX(8))
    funUS(multiF, 2, 3)
    print('引入模块函数 %d' % module1.add(3, 3))
    dirF()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
