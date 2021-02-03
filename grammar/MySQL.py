import mysql.connector

"""
出现错误：authentication plugin 'calling_sha2_password' is not supported.
解决方式：python3 -m pip install mysql-connector-python
"""
db = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="root",  # 数据库密码
    database="springboot"
)

cursor = db.cursor()
# cursor.execute("SHOW DATABASES")
# for x in cursor:
#     print(x)


cursor.execute("SELECT * FROM t")

result = cursor.fetchall()  # fetchall() 获取所有记录
for x in result:
    print(x)
