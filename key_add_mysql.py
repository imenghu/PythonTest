import random
import string
import pymysql


def GenKey(length):
    chars = string.ascii_letters + string.digits
    return ''.join([random.choice(chars) for i in range(length)])


def SaveKey(content):
    with open('Result Key.txt', 'a') as f:
        f.write(content)
        f.write('\n')


def save_to_mysql(code):
    # 将数据保存到mysql数据库
    host = "127.0.0.1"
    user = "root"
    port = 3306
    pass_ = "111111"
    db = "active"
    #  设置数据库连接相关信息
    connect = pymysql.connect(
        host=host,
        port=port,
        user=user,
        password=pass_,
        db=db,
        charset='utf8')
    cursor = connect.cursor()
    #  链接数据库并设置游标
    sql = "insert into activeCode(code) VALUES ('%s')"
    data = code

    # 执行sql语句
    result = cursor.execute(sql % data)
    # 千万不要忘记做这一步的操作
    connect.commit()
    # print(result)
    # 关闭连接，游标和连接都要关闭
    cursor.close()
    connect.close()


if __name__ == '__main__':
    for i in range(20):
        value = GenKey(20)
        print(value)
        SaveKey(value)
        save_to_mysql(value)
