#coding=utf-8
import time,sys
sys.path.append('./interface')
sys.path.append('./db_fixture')
from HTMLTestRunner import HTMLTestRunner
import unittest
import smtplib
from db_fixture import test_data
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

test_dir='./interface'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='*_test.py')

def sendReport(f):
	sender='ganlp@justcall.cn'
	receiver='ganlp@justcall.cn'
	f=open(f,"rb")
	mail_body=f.read()
	f.close()
	msg=MIMEText(mail_body,_subtype='html',_charset='utf-8')
	msg['From']=Header("Lillian",'utf-8')
	msg['To']=Header("甘",'utf-8')
	msg['Subject']=u'Auto-test Report'
	msg['date']=time.strftime('%a,%d %b %Y %H:%M:%S %z')
	smtpserver='192.168.6.107'
	smtp=smtplib.SMTP(smtpserver)
	username="ganlp@justcall.cn"
	password="200913138003"
	smtp.login(username,password)
	smtp.sendmail(sender,receiver,msg.as_string())
	smtp.quit()
	print 'email has send out!'

if __name__=="__main__":
	test_data.init_data()
	now=time.strftime("%Y-%m-%d %H_%M_%S")
	filename="./report/"+now+'_result.html'
	fp=open(filename,'wb')
	runner=HTMLTestRunner(stream=fp,title='stream Manage System Interface Test Report',description='Implementation Example with:')
	runner.run(discover)
	fp.close()
	sendReport(filename)	