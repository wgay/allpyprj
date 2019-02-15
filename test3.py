#! /usr/bin/python3

str = 'Runoob'
print(str) # 输出字符串
print(str[0:-1])#输出第一个到倒数第二个的所有字符
print(str[0])#输出字符串第一个字符
print(str[2:5])#输出从第三个开始到第五个的字符
print(str[2:])#输出从第三个开始的后的所有字符
print(str * 2) #输出字符串两次
print(str + "TEST") #连接字符串


list = ['abcd',786,2.23,'runoob',70.2]
tinylist=[123,'runoob']
print(list)#输出完整列表
print(list[0])#输出列表第一个元素
print(list[1:3])#从第二个开始输出到第三个元素
print(list[2:])#输出从第三个元素开始的所有元素
print(tinylist * 2)# 输出两次列表
print(list + tinylist) #链接列表


'''
1. List写在方括号之间，元素用逗号隔开
2.和字符串一样，list可以被索引和切片
3.List可以使用+操作费进行链接
4.List中的元素是可以改变的
'''

a = [1,2,3,4,5,6]
a[0] = 9
a[2:5] = [13,14,15]
print(a)
