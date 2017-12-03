#先导入pymysql代码库
import pymysql

def connDB():
    #连接数据库，需要数据库的信息：ip地址，端口号，用户名和密码，数据库名称
    conn = pymysql.Connect(host="localhost", user="root", password="root",database="pirate", port=3306,charset='utf8')
    #查询hd_user表中所有的数据，并且倒叙打印
    sql = "SELECT * FROM hd_user ORDER by id DESC"

    #在代码中执行这条sql语句时，先要获取数据库的游标cursor
    curs = conn.cursor()

    #通过游标执行sql语句
    curs.execute(sql)
    #获取数据库最新的记录，需把数据库所有的记录倒叙排练，然后用fetchone录（）方法获取第一条记录，即数据库的最新记录
    #获取所有查询结果，用fetchall（）
    result = curs.fetchone()
    return result
    #result = cur,fetchall()

if __name__ == '__main__':
    print(connDB())