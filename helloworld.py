#coding=utf-8
print("beginning to connect sqlite3")
###使用sqlite###
import sqlite3
conn=sqlite3.connect('//Users//wuwen//python//studypython//study-python//test.db')
cur=conn.cursor()
sql="create table if not exists 't_user'('id' int,'name' char(24),'password' char(24))"
str=cur.execute(sql)
print("create table successfully")
conn.commit()
cur.close()

#write file#
file1=open("wuwen.txt","w")
file1.write("你好 \n")
file1.close()

#append file#
file2=open("wuwen.txt","a")
file2.write("李小喵")
file2.close()

#read file#
file=open("wuwen.txt","r")
print(file.read())
file.close()
