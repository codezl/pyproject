#!/usr/bin/python
# -*- coding: UTF-8 -*-
import sys
import os


if __name__ == '__main__':
    print(sys.platform)
    print(os.environ["HOMEPATH"])
    print(os.getcwd())
    print(os.getlogin())
    print(os.getenv)
    cmd = "ipconfig"
    os.system(cmd)
    print('作为主程序运行')
    str2 = input("请输入:")
    print("输入值："+str(str2))
else:
    print('package_runoob 初始化')