"""
函数装饰器
"""
import pymysql


def log(func):
    def wrapper(sname):
        """
            向利用wrapper向stustrg表中插入数值
        :return:
        """
        func(sname)
        connection = pymysql.connect(host="localhost", user="root", password="123456", port=8888, database="woniudb")
        cursor = connection.cursor()
        cursor.execute("insert into stustrg values('{}')".format(sname))
        connection.commit()
        cursor.close()
        if connection:
            connection.close()
            print("连接已经关闭")
        else:
            print("关闭连接失败")
    return wrapper