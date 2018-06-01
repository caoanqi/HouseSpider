# -*-coding:utf-8-*-

import mysql.connector
from HouseSpider import settings

MYSQL_HOSTS = settings.MYSQL_HOSTS
MYSQL_USER = settings.MYSQL_USER
MYSQL_PASSWORD = settings.MYSQL_PASSWORD
MYSQL_PORT = settings.MYSQL_PORT
MYSQL_DB = settings.MYSQL_DB

cnx = mysql.connector.connect(user=MYSQL_USER, password=MYSQL_PASSWORD, host=MYSQL_HOSTS, database=MYSQL_DB,
                              use_unicode=True)
cur = cnx.cursor(buffered=True)


class Sql:
    @classmethod
    def insert_netdata(cls, title, address, other, updateTime, price, lookCount, area):
        sql = 'INSERT INTO house_renting (title, address, other, updateTime,price,lookCount,area) VALUES (%(title)s, %(address)s, %(other)s,%(updateTime)s,%(price)s,%(lookCount)s,%(area)s)'
        value = {
            'title': title,
            'address': address,
            'other': other,
            'updateTime': updateTime,
            'price': price,
            'lookCount': lookCount,
            'area': area
        }

        # 如果已经存在同一条数据，则删除旧的数据
        if Sql.select_house_renting(title) > 0:
            Sql.clear_id_house_renting(title)

        cur.execute(sql, value)
        cnx.commit()

    @classmethod
    def clear_house_renting(cls):
        sql = 'DELETE FROM house_renting'
        cur.execute(sql)
        cnx.commit()

    @classmethod
    def clear_id_house_renting(cls, title):
        sql = 'DELETE FROM house_renting WHERE id=%(id)s'
        params = {
            'id': Sql.select_id_house_renting(title)
        }
        cur.execute(sql, params)
        cnx.commit()

    @classmethod
    def count_house_renting(cls):
        sql = 'SELECT COUNT(*) FROM house_renting'
        cur.execute(sql)
        return cur.fetchone()

    @classmethod
    def select_house_renting(cls, title):
        sql = "SELECT EXISTS(SELECT 1 FROM house_renting WHERE title=%(title)s)"
        value = {
            'title': title
        }
        cur.execute(sql, value)

        if cur.arraysize <= 0:
            return 0
        else:
            return 1

    @classmethod
    def select_id_house_renting(cls, title):
        sql = 'SELECT * FROM house_renting WHERE title=%(title)s'
        param = {
            'title': title
        }
        cur.execute(sql, param)
        for id_house_renting in cur:
            return id_house_renting[0]

    # 通用插入内容
    @classmethod
    def insert_content_house_renting(cls, news_id, content):

        sql = 'UPDATE house_renting SET content=%(content)s WHERE id=%(id)s'
        param = {
            'id': news_id,
            'content': content
        }
        cur.execute(sql, param)
        rowcount = cur.rowcount
        if rowcount > 0:
            return True
        else:
            return False

    @classmethod
    def select_price_with_area(cls, area):
        sql = 'select price from house_renting WHERE area=%(area)s'
        params = {
            'area': area
        }
        cur.execute(sql, params)

        return cur.fetchall()

    # 获取最小价格
    @classmethod
    def select_min_price(cls, area):
        sql = 'select min(price) from house_renting WHERE area=%(area)s'
        params = {
            'area': area
        }
        cur.execute(sql, params)

        result = cur.fetchone()
        if result is None:
            return 0
        else:
            if result[0] is None:
                return 0
            else:
                return result[0]

    # 获取最大价格
    @classmethod
    def select_max_price(cls, area):
        sql = 'select max(price) from house_renting WHERE area=%(area)s'
        params = {
            'area': area
        }
        cur.execute(sql, params)

        result = cur.fetchone()
        if result is None:
            return 0
        else:
            if result[0] is None:
                return 0
            else:
                return result[0]

    # 清空表数据
    @classmethod
    def clear_table(cls):
        sql = 'DELETE FROM house_renting'
        cur.execute(sql)
