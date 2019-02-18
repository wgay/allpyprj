#! /usr/bin/python3
#可写函数说明

'''
python 使用 lambda 来创建匿名函数。

所谓匿名，意即不再使用 def 语句这样标准的形式定义一个函数。

lambda 只是一个表达式，函数体比 def 简单很多。
lambda的主体是一个表达式，而不是一个代码块。仅仅能在lambda表达式中封装有限的逻辑进去。
lambda 函数拥有自己的命名空间，且不能访问自己参数列表之外或全局命名空间里的参数。
虽然lambda函数看起来只能写一行，却不等同于C或C++的内联函数，后者的目的是调用小函数时不占用栈内存从而增加运行效率。
语法
lambda 函数的语法只包含一个语句，如下：

lambda [arg1 [,arg2,.....argn]]:expression
'''
import  sys
sum = lambda  arg1,arg2:arg1+arg2
#调用sum函数
print("相加后的值为：",sum(10,20))
print("相加后的值为：",sum(20,20))

total = 0 #这是一个全局变量
#可写函数说明
def sum(arg1,arg2):
    #返回2个参数的和
    total = arg1 + arg2
    print("函数内是局部变量：",total)
    return total

#调用sum函数
sum(10,20)
print("函数外是全局变量",total)


'''
global 和 nonlocal关键字
当内部作用域想修改外部作用域的变量时，就要用到global和nonlocal关键字了。

以下实例修改全局变量 num：
'''

num = 1
def fun1():
    global num #需要使用global关键字声明
    print(num)
    num = 123
    print(num)
fun1()
print(num)



def outer():
    num = 10
    def inner():
        nonlocal num # nonlocal关键字声明
        num = 100
        print(num)
    print(num)
    inner()
    print(num)
outer()

print(sys.path)

import user_name


