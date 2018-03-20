#encoding=utf-8
import requests
import unittest

class  GetEventListTest(unittest.TestCase):
	def setUp(self):
		self.url="http://127.0.0.1:8000/api/get_event_list/"

	def test_get_event_null(self):
		'''id为空'''
		r=requests.get(self.url,params={'eid':''})
		result=r.json()
		print(result)
		self.assertEqual(result['status'],10021)
		self.assertEqual(result['message'],"parameter error")

	def test_get_event_success(self):
		'''查询成功'''
		r=requests.get(self.url,params={'eid':'1'})
		result=r.json()
		print(result)
		self.assertEqual(result['status'],200)
		self.assertEqual(result['message'],"success")
		self.assertEqual(result['data']['name'],'Just')
		self.assertEqual(result['data']['address'],'software apartment')
		self.assertEqual(result['data']['start_time'],'2017-11-08T06:23:26Z')

if __name__=='__main__':
	unittest.main()



		