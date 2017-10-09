import MySQLdb


# 打开数据库
db = MySQLdb.connect("localhost", "testuser", "testuser123", "TESTDB")


# 使用cursor()方法获取操作游标
cursor = db.cursor()

# 使用execute方法执行sql语句
cursor.execute("SELECT VERSION()")

# 如果数据库表已经存在使用 execute() 方法删除表
cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# 创建数据表SQL 语句
sql = """CREATE TABLE EMPLOYEE(
        FRIST_NAME CHAR(20) NOT NULL,
        LAST_NAME CHAR(20),
        AGE INT,
        SEX CHAR(1),
        INCOME FLOAT)"""
cursor.execute(sql)        


# 使用fetchone()方法获取一条数据
data = cursor.fetchone()


# SQL 插入语句
sql = """INSERT INTO EMPLOYEE(FIRST_NAME,LAST_NAME,AGE,SEX,INCOME)
        VALUES('MAC','Mohan',20,'M', 2000)"""

try:
    # 执行sql语句
    cursor.execute(sql)

    # 获取所有记录列表
    results = cursor.fetchall()
    for row in results:
        fname = row[0]
        lname = row[1]
        age = row[2]
        sex = row[3]
        income = row[4]
        print("fname=%s, lname=%s, age=%d, sex=%s, income=%d" % \
                (fname, lname, age, sex, income))
    # 提交到数据库
    db.commit()
except:
    print("Error: unable to fetch data")
    # rollback in case there is any error
    db.rollback()        


print("database version : %s" % data)

# 关闭数据库

db.close()