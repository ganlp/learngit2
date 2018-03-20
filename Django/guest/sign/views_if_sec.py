#coding=utf-8
from django.contrib import auth as django_auth
import hashlib

def user_auth(request):
	get_http_auth=request.MATA.get('HTTP_AUTHORIZATION',b'')
	auth=get_http_auth.split()
	try:
		auth_parts=base64.b64decode(auth[1].decode('iso-8859-1').partition(':'))
	except IndexError:
		return "null"
	userid,password=auth_parts[0],auth_parts[2]
	print userid,password
	user=django_auth.authenticate(username=userid,password=password)
	if user is not None and user.is_active:
		django_auth.login(request,user)
		return "success"
	else:
		return "fail"

	get_http_auth=request.MATA.get('HTTP_AUTHORIZATION',b'')

def get_event_list(request):
	auth_result=user_auth(request)
	if auth_result=="null":
		return JsonResponse({'status':10011,'message':'user auth null'})

	if auth_result=="fail":
		return JsonResponse({'status':10012,'message':'user auth fail'})

	eid=request.GET.get("eid","")
	name=request.GET.get("name","")

	if eid=='null':
		return JsonResponse({'status':10021,'message':'parameter error'})

	if eid==1 and name=='QQ game':
		return JsonResponse({'status':200,'message':'success','data':{'name':'QQ game','address':'会展中心'}})

def user_sign(request):  #用户签名+时间戳
	client_time=reques.POST.get('time','')
	client_sign=request.POST.get('sign','')
	if client_time=='' or client_sign=='':
		return "sign null"

	now_time=time.time()
	server_time=str(now_time).split('.')[0]
	time_difference=int(server_time)-int(client_time)
	if time_difference>=60:
		return "timeout"

	md5=hashlib.md5()
	sign_str=client_time+"&Guest-Bugmaster"
	sign_bytes_utf8=sign_str.encode(encoding="utf-8")
	md5.update(sign_bytes_utf8)
	server_sign=md5.hexdigest()
	if server_sign!=client_sign:
		return "sign error"
	else:
		return "sign right"		

#添加发布会接口
def add_event(request):
	sign_result=user_sign(request)
	if sign_result=="sign null":
		return JsonResponse({'status':10011,'message':'user sign null'})
	elif sign_result=="time out":
		return JsonResponse({'status':10012,'message':'user sign timeout'})
	elif sign_result=="sign error":
		return JsonResponse({'status':10013,'message':'user sign error'})