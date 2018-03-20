#coding=utf-8
import sys
sys.path.append('../db_fixture')
from mysql_db import DB 

datas={
	'sign_event':[
	{'id':1,'name':'QQ game','status':1,'address':'会展中心','start_time':'2017-12-20 12:00:00'},],
	'sign_guest':[
	{'id':1,'realname':'alen','phone':13511001100,'email':'alen@mail.com','sign':0,'event_id':1},],
}

def init_data():
	db=DB()
	for table,data in datas.items():
		db.clear(table)
		for d in data:
			db.insert(table,d)
	db.close()

if __name__=='__main__':
	init_data()