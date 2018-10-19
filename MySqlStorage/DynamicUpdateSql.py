# 动态 sql 修改
import pymysql

data = {
    'id': '20120003',
    'name': 'Bob',
    'age': 20
}

table = 'students'
keys = ','.join(data.keys())
values = ','.join(['%s'] * len(data))
db = pymysql.connect(host='localhost', user='root', password='123456', port=3306, db='spiders')
cursor = db.cursor()
sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                     values=values)
update = ','.join([" {key} = %s".format(key=key) for key in data])
sql += update
try:
    if cursor.execute(sql, tuple(data.values()) * 2):
        print('Success')
        db.commit()
except:
    print('Failed')
    db.rollback()
db.close()
