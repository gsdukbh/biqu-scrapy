# -*- coding: utf-8 -*-
import  pymysql

connection =pymysql.connect(host='120.78.148.61',
                            user='t',
                            passwd='JztHdLHpzsWWnf67',
                            db='t',
                            charset='utf8mb4')
cursor = connection.cursor()
SQL ="""CREATE TABLE novel_list (
novel_id INT not null AUTO_INCREMENT,
novel_name VARCHAR ( 50 ),
novel_author VARCHAR ( 50 ),
novel_type VARCHAR ( 20 ),
novel_info VARCHAR ( 500 ),
novel_cover VARCHAR ( 200 ),
novel_uptime VARCHAR ( 50 ),
novel_source VARCHAR ( 100 ) ,
primary key (novel_id)
)"""

cursor.execute(SQL)

