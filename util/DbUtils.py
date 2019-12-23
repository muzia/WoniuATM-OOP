"""
	想要把数据库的增删改查四个操作封装成一个类(工具类)
"""
import pymysql
from util.DataBaseConfig import *


class DatabaseUtil(object):
    """
        数据库的操作工具类
    """


    def __init__(self, user, password, database, host="localhost", port=8888, charset="utf8", autocommit=True,
                 cursorclass=pymysql.cursors.DictCursor):
        """
            init方法中完成数据库的连接
        """

        self.connection = pymysql.connect(host=host, user=user, password=password, database=database, charset=charset,
                                          port=port, autocommit=autocommit, cursorclass=cursorclass)

    def update(self, sql):
        """
            对数据表执行修改操作
                insert update delete
            @sql 要执行的sql语句
        """

        # 获取游标
        self.cursor = self.connection.cursor()
        # 执行sql语句
        try:
            # try中放可能会产生异常的代码
            self.cursor.execute(sql)
            # self.connection.commit()
        except:
            # 回滚上面的错误操作.让代码还原到更改之前
            self.connection.rollback()
        finally:
            # 关闭游标
            self.cursor.close()

    def select(self, sql):
        """
            从数据库中查询数据
        """
        # 获取游标
        self.cursor = self.connection.cursor()
        # 执行sql语句
        try:
            # try中放可能会产生异常的代码
            self.cursor.execute(sql)
            # 抓取全部的数据
            result = self.cursor.fetchall()
            return result
        except:
            print("Error:查询数据库失败!")
        finally:
            # 关闭游标
            self.cursor.close()

    def __del__(self):
        """
            关闭数据库连接
        """
        self.connection.close()
