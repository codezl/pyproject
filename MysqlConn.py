# a mysql demo
# -*- coding: UTF-8 -*-
# 为使用的包不要引入避免部署到服务器缺少module报错
# import charset_normalizer.constant
# import mysql.connector
# import MySQLdb
import pymysql as pymysql


# 方法一
def conn(host, port, user, psw, database):
    return pymysql.connect(host=host, user=user, port=port, password=psw, charset='utf8', database=database)


def tstCon():
    con = conn('localhost', 3306, 'root', 'root', 'test')
    cur = con.cursor()
    cur.execute('select * from user')
    data = cur.fetchall()
    print(data)
    cur.close()
    con.close()


# 方法二
# db = MySQLdb.connect(host="localhost",
#                      user="root",
#                      password="root",
#                      db="test")


# def conn1():
#     cursor = db.cursor()
#
#     # 使用execute方法执行SQL语句
#     cursor.execute("SELECT VERSION()")
#
#     # 使用 fetchone() 方法获取一条数据
#     data = cursor.fetchone()
#
#     print("Database version : %s " % data)
#
#     # 关闭数据库连接
#     db.close()


# if __name__ == "__main__":
    # conn1()
    # tstCon()
