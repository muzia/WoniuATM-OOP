# from 包名.文件名 import 类名/函数名/全局变量
from services.AccountServices import AccountServices


def show_welcome_view():
    while 1:
        tips = """1.登录 2.注册 3.退出"""
        print(tips)
        choose = input("enter choose")
        account_services = AccountServices()
        if choose == "1":
            if account_services.login():
                main_view()
        elif choose == "2":
            account_services.register()
        elif choose == "3":
            break
        else:
            print("没有改选项请重新选择")
    print("欢迎下次使用!")



def main_view():
    tips = "1.查询 2取款 3.转账"
    print(tips)
    input("啦啦啦")


if __name__ == '__main__':
    """
        程序的总入口

        代码的执行流程是从入口开始:main.一个程序中可以有多个main方法(在不同的模块要做测试.最简单的方式就是main)
        .但是最终代表执行入口的只有一个地方.
        
        通过入口显示界面信息

    """
    # Ctrl + D 复制当前行到下一行 Ctrl + Y 删除当前行
    show_welcome_view()

