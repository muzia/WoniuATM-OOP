import pymysql


class AccountDao(object):
    """
        Dao负责对接数据库.给Service提供数据支持!
    """

    def find_account(self,username,userpwd):
        """
            只有class名称的首字母是大写的.变量,方法,函数名都是全小写的.多个单词使用_拼接
            查找账户
        :param username 用户录入的用户名
        :param userpwd  用户录入的密码
        :return: 查找到的用户对象
        """
        from util.DbUtils import DatabaseUtil
        from model.Account import Account
        du = DatabaseUtil(user="root",password="123456",database="wn15")
        sql = "select * from account where name = '{}' and pwd = '{}'".format(username,userpwd)
        result = du.select(sql)

        account = Account()
        account.account_id = result[0].get("id")
        account.account_nickname = result[0].get("name")
        account.account_pwd = result[0].get("pwd")
        account.account_balance = result[0].get("balance")

        return account