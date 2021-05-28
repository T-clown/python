import mysql.connector
from loguru import logger

"""
出现错误：authentication plugin 'calling_sha2_password' is not supported.
解决方式：python3 -m pip install mysql-connector-python
"""
db = mysql.connector.connect(
    host="localhost",  # 数据库主机地址
    user="root",  # 数据库用户名
    passwd="root123456",  # 数据库密码
    database="springboot"
)

cursor = db.cursor()


class SpringBoot:
    __insert_sql = "INSERT INTO master.springboot_user (username, gender, birthday, email, phone, create_time, update_time, is_deleted) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s);";
    __select_sql = "SELECT * FROM master.springboot_user";
    __count_sql = "SELECT COUNT(*) FROM master.springboot_user";

    def insert(self, data):
        cursor.executemany(self.__insert_sql, data)
        db.commit()
        logger.info("数据插入 {} 条 ".format(cursor.rowcount))

    def select(self):
        cursor.execute(self.__select_sql)
        data = cursor.fetchall()
        for x in data:
            logger.info("数据:{}".format(x))

    def count(self):
        cursor.execute(self.__count_sql)
        count = cursor.fetchone()[0]
        logger.info("数据统计 {} 条 ".format(count))


if __name__ == "__main__":
    sb = SpringBoot()
    data = [('666', 'MALE', '2021-05-12 14:19:02', "", "", '2021-05-12 14:19:13', '2021-05-12 14:19:16', 0)]

    sb.count()
