#! /usr/bin/python3


'''

Python 定义函数使用 def 关键字，一般格式如下：

def 函数名（参数列表）:
    函数体
默认情况下，参数值和参数名称是按函数声明中定义的顺序匹配起来的。
'''
def hello():
    print("Hello World!")

def area(width,height):
    return width * height

def print_welcome(name):
    print("Welcome",name)

print_welcome("Runoob")
w = 4
h = 5
print("width = ",w,"height = ",h,"area = ",area(w,h))
hello()

'''
函数调用
定义一个函数：给了函数一个名称，指定了函数里包含的参数，和代码块结构。

这个函数的基本结构完成以后，你可以通过另一个函数调用执行，也可以直接从 Python 命令提示符执行。

如下实例调用了 printme() 函数：
'''
#定义函数
def printme(str):
#打印任何传入的字符串
    print(str)
    return
#调用函数
printme("我要调用用户自定义函数！")
printme("再次调用同一函数")



