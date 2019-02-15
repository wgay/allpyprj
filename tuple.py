#! /usr/bin/python3

tuple = ('abcd',786,2.23,'runoob',70.2)
tinytuple = (123,'runoob')
print(tuple) #输出完整元组
print(tuple[0])#输出元组的第一个元素
print(tuple[1:3])#输出从第二个元素开始到第三个元素
print(tuple[2:]) #输出从第三个元素开始的所有元素
print(tinytuple * 2)#输出两次元组
print(tuple+tinytuple)#连接元组

# tup1 = ()  tup2 = (20,) 一个元素，需要在元素后添加逗号，注意string ，list，tuple都属于sequence（序列）
'''
1.与字符串一样，元组的元素不能修改
2.元组也可以被索引和切片，方法一样
3.注意构造包含0或1个元素的元组的特殊语法规则
4.元组也可以使用+操作符进行拼接
'''