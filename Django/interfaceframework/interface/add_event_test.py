#coding=utf-8
import unittest
import requests
import os,sys,time,hashlib
parentdir=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0,parentdir)
from db_fixture import test_data

class AddEventTest(unittest.TestCase):
	def setUp(self):
		self.base_url="http://127.0.0.1:8000/api/add_event/"

	def tearDown(self):
		print self.result

	def test_add_event_all_null(self):
		payload={'eid':'','name':'','address':'','start_time':''}
		r=requests.post(self.base_url,data=payload)
		self.result=r.json()
		self.assertEqual(self.result['status'],10021)
		self.assertEqual(self.result['message'],'parameter error')

	def test_add_event_eid_exist(self):
		payload={'eid':1,'name':'just app','address':'shenzhen','start_time':'2017'}
		r=requests.post(self.base_url,data=payload)
		self.result=r.json()
		self.assertEqual(self.result['status'],10022)
		self.assertEqual(self.result['message'],'event id already exists')

	def test_add_event_name_exist(self):
		payload={'eid':11,'name':'QQ game','address':'beijing','start_time':'2017-10-11 12:00:00'}
		r=requests.post(self.base_url,data=payload)
		self.result=r.json()
		self.assertEqual(self.result['status'],10023)
		self.assertEqual(self.result['message'],'event name already exists')

	def test_add_event_data_type_error(self):
		payload={'eid':11,'name':'一加','address':'beijing','start_time':'2017'}
		r=requests.post(self.base_url,data=payload)
		self.result=r.json()
		self.assertEqual(self.result['status'],10024)
		self.assertIn('start_time format error.',self.result['message'])

	def test_add_event_success(self):
		payload={'eid':11,'name':'apple','address':'shuilifang','start_time':'2017-05-10 12:00:00'}
		r=requests.post(self.base_url,data=payload)
		self.result=r.json()
		self.assertEqual(self.result['status'],200)
		self.assertEqual(self.result['message'],'add event success')

if __name__=='__main__':
	test_data.init_data()
	unittest.main()