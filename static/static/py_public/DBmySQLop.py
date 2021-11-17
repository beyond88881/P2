# import MySQLdb
import pymysql
# from DBUtils.PooledDB import PooledDB
from dbutils.pooled_db import PooledDB

class OPMysql(object):
    __pool = None

    def __init__(self):
        # 构造函数，创建数据库连接、游标
        self.coon = OPMysql.getmysqlconn()
        self.cur = self.coon.cursor(cursor=pymysql.cursors.DictCursor)

    # 数据库连接池连接
    @staticmethod
    def getmysqlconn():
        if OPMysql.__pool is None:
            __pool = PooledDB(creator=pymysql, mincached=1, maxcached=20, host="localhost", user="root", passwd="123456",
                              db="project", port=3306, charset="utf8")
            print(__pool)
        return __pool.connection()

    # 插入\更新\删除sql
    def op_insertDeleteUpdate(self, sql):
        print('op_insert', sql)
        try:
            insert_num = self.cur.execute(sql)
            print('mysql sucess ', insert_num)
            self.coon.commit()
        except:
            self.coon.rollback()
            print("Error: unable to operate data")
        return insert_num

    # 查询
    def op_select(self, sql):
        print('op_select', sql)
        try:
            self.cur.execute(sql)  # 执行sql
            # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
            # fetchall(): 接收全部的返回结果行.
            # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
            select_res = self.cur.fetchall()  # 返回结果为字典 select_res = self.cur.fetchone()
            print('op_select', select_res)
            return select_res
        except:
            print("Error: unable to fecth data")

    # 获取表的所有字段
    def getFields(self, tableNameX):
        sql = "select * from " + tableNameX
        try:
            self.cur.execute(sql)  # 执行sql
            select_res = self.cur.fetchone()  # 返回结果为字典
            return select_res
        except:
            print("Error20040501: unable to fecth data")

    def getFieldType(self, tableNameX):
        sql = "select column_name, DATA_TYPE from information_schema.COLUMNS where TABLE_NAME='" + tableNameX + "';"
        dic = {}
        try:
            self.cur.execute(sql)  # 执行sql
            select_res = self.cur.fetchall()  # 返回结果为字典
            for field in select_res:  # for field in cur:
                print(field[0] + ":" + field[1])
                dic[field[0]] = field[1]
            return dic
        except:
            print("Error20040502: unable to fecth data")

    # 释放资源
    def dispose(self):
        self.coon.close()
        self.cur.close()

    def __del__(self):
        self.dispose()
