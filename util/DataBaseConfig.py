import pymysql

host="localhost"
user="root"
password="123456"
database="wn15"
port=3306
charset="utf8"
autocommit=True
cursorclass=pymysql.cursors.DictCursor 
# 默认是((1, '张三'), (2, '张三')) ((),())
# 改成字典:[{'id': 1, 'name': '张三'}, {'id': 2, 'name': '张三'}]