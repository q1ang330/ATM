# Author:q1.ang
import os
import sys
print(os.path.abspath(__file__))#绝对路径
print(os.path.dirname(os.path.abspath(__file__))) #返回目录名，不要文件名
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) #返回目录名，不要文件名
BASE_DIR=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
sys.path.append(BASE_DIR)	#添加环境变量
spending=None

from core import main

main.run(spending)