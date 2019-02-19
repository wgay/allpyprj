# ! /usr/bin/python3
# filename: using_name.py

import mysql.connector

mydb = mysql.connector.connect(
    host="192.168.162.130",#数据库主机地址
    user="robot",#数据库用户名
    passwd="root123456" #数据库密码
)

mycursor = mydb.cursor()
mycursor.execute("drop database test1")
