import pymysql
# Alt + Shift +上下键 上下移动代码
from Wrapper.FunctionWrapper import *


@log
def method(sname):
    """
        利用method向student表中插入学生记录
    :return:
    """
    connection = pymysql.connect(host="localhost",user="root",password="123456",port=8888,database="woniudb")
    cursor = connection.cursor()
    cursor.execute("insert into student values(0,'{}','男',19,100.0)".format(sname))
    connection.commit()
    cursor.close()
    if connection:
        connection.close()
        print("连接已经关闭")
    else:
        print("关闭连接失败")


method('孙七')

