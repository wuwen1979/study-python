#coding=utf-8
print("哈哈")
###使用sqlite###
import sqlite3
conn=sqlite3.connect('//Users//wuwen//python//studypython//study-python//test.db')
cur=conn.cursor()
sql="create table if not exists 't_user'('id' int,'name' char(24),'password' char(24))"
str=cur.execute(sql)
print("create table successfully")
conn.commit()
cur.close()
