#coding=utf-8
import unittest
import requests
import os,sys,time
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

class  GetEventListTest(unittest.TestCase):
	''' 获取Event列表 '''

	def setUp(self):
		self.base_url="http://127.0.0.1:8000/api/get_event_list/"

	def teardown(self):
		print self.result

	def test_get_event_list_eid_null(self):
		r=requests.get(self.base_url,params={'eid':''})
		self.result=r.json()
		print self.result
		self.assertEqual(self.result['status'],10021)
		self.assertEqual(self.result['message'],'parameter error')

	def test_get_event_list_eid_success(self):
		r=requests.get(self.base_url,params={'eid':1})
		self.result=r.json()
		print self.result
		self.assertEqual(self.result['status'],200)
		self.assertEqual(self.result['message'],'success')
		self.assertEqual(self.result['data']['name'],u'QQ game')
		self.assertEqual(self.result['data']['address'],u'会展中心')
		self.assertEqual(self.result['data']['start_time'],'2017-12-20T12:00:00Z')

	def test_get_event_list_eid_fail(self):
		r=requests.get(self.base_url,params={'eid':2})
		self.result=r.json()
		print self.result
		self.assertEqual(self.result['status'],10022)
		self.assertEqual(self.result['message'],'query result is empty')

	def test_get_event_list_name_null(self):
		r=requests.get(self.base_url,params={'name':''})
		self.result=r.json()
		print self.result
		self.assertEqual(self.result['status'],10021)
		self.assertEqual(self.result['message'],'parameter error')

	def test_get_event_list_name_success(self):
		r=requests.get(self.base_url,params={'name':'QQ game'})
		self.result=r.json()
		print self.result
		self.assertEqual(self.result['status'],200)
		self.assertEqual(self.result['message'],'success')
		self.assertEqual(self.result['data'][0]['name'],u'QQ game')
		self.assertEqual(self.result['data'][0]['address'],u'会展中心')
		self.assertEqual(self.result['data'][0]['start_time'],'2017-12-20T12:00:00Z')

	def test_get_event_list_name_fail(self):
		r=requests.get(self.base_url,params={'name':'xiaomi'})
		self.result=r.json()
		print self.result
		self.assertEqual(self.result['status'],10022)
		self.assertEqual(self.result['message'],'query result is empty')




if __name__=='__main__':
	test_data.init_data()
	unittest.main()