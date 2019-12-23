class AccountServices(object):
    """
        这是Account的业务类.里面封装Account的相关业务
            1.查询账户
            2.取款
            3.存款
            4.转账
            5.查看交易记录(流水!)
    """

    def __init__(self):
        # locally
        from dao.AccountDao import AccountDao
        self.ad = AccountDao()

    def login(self):
        # 第一步:获取键盘录入的用户名和密码
        username = input("enter name")
        userpwd = input("enter pwd")
        # 第二步:向数据库发送请求验证用户名和密码是否正确
        account = self.ad.find_account(username,userpwd)
        # 第三步: 判断账户是否存在
        if account:
            print("登录成功,当前登录用户为:{}".format(account.account_nickname))
            return True
        else:
            print("登录失败!")
            return False

    def register(self):
        pass

    def query(self):
        pass

    def with_draw(self):
        pass

    def deposit(self):
        """
        存款
        :return:
        """
        pass

    def transfer(self):
        pass

    def show_histroy(self):
        """
        查看流水
        :return:
        """
        pass