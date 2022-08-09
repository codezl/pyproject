# a mysql demo
# -*- coding: UTF-8 -*-
import charset_normalizer.constant
import mysql.connector
import MySQLdb
import pymysql as pymysql


def conn(host,port,user,psw):
    pymysql.connect


def conn1():
    db = MySQLdb.connect(host="localhost",
                         user="root",
                         password="root",
                         db="test")
    cursor = db.cursor()

    # 使用execute方法执行SQL语句
    cursor.execute("SELECT VERSION()")

    # 使用 fetchone() 方法获取一条数据
    data = cursor.fetchone()

    print("Database version : %s " % data)

    # 关闭数据库连接
    db.close()


if __name__ == "__main__":
    conn1()