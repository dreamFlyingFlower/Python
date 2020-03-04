# python操作mysql
# python中的orm框架是SQLAlchemy,如何使用百度
import  pymysql
conn = pymysql.connect(host="127.0.0.1", port=3306, user="root", passwd="52LDforever", db="simpleoa")  # 创建连接
cursor = conn.cursor()  # 创建游标
# 执行sql,返回影响行数,不管是增删改查都是返回影响行数,默认不自动提交事务,需要手动提交事务
row = cursor.execute("select * from ti_user")
row1 = cursor.executemany("delete from ti_user where user_id in ({0},{1})",[1,2])# 执行多次
conn.commit() # 事务提交
print(row)
print(cursor.fetchone())  # 查询一条数据,返回一个元组
print(cursor.fetchall())  # 从上次游标的位置开始,查询所有数据,返回元组
cursor.close()
conn.close()

