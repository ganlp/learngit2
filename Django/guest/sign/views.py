from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from sign.models import Event,Guest
import bootstrap3
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.shortcuts import render,get_object_or_404

# Create your views here.
def index(request):
	#return HttpResponse("Hello Django!")
	return render(request,"index.html")

def login_action(request):
	if request.method=='POST':
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		user=auth.authenticate(username=username,password=password)
		if user is not None:
			auth.login(request,user)
			request.session['user']=username
			response=HttpResponseRedirect('/event_manage/')
			return response
		else:
			return render(request,'index.html',{'error':'username or password error!'})
	else:
		return render(request,'index.html',{'error':'username or password error!'})		


def login_action2(request):
	if request.method=='POST':
		username=request.POST.get('username','')
		password=request.POST.get('password','')
		if username=='ganlp' and password=='111111':
			#return HttpResponse("login success!")
			response=HttpResponseRedirect('/event_manage/')
			#response.set_cookie('user',username,3600)  #add browser cookie
			request.session['user']=username
			return response
		else:
			return render(request,'index.html',{'error':'username or password error!'})
	else:
		return render(request,'index.html',{'error':'username or password error!'})

@login_required
def event_manage(request):
	#username=request.COOKIES.get('user','') #read browser cookie
	event_list=Event.objects.all()
	username=request.session.get('user','')
	#return render(request,"event_manage.html",{"user":username})
	return render(request,"event_manage.html",{"user":username,"events":event_list})

@login_required
def search_name(request):
	username=request.session.get('user','')
	search_name=request.GET.get("name","")
	event_list=Event.objects.filter(name__contains=search_name)
	return render(request,"event_manage.html",{"user":username,"events":event_list})

#@login_required
def guest_manage(request):
	username=request.session.get('user','')
	guest_list=Guest.objects.all()
	paginator=Paginator(guest_list,1)
	print paginator.count
	page=request.GET.get('page')
	print page
	try:
		contacts=paginator.page(page)
	except PageNotAnInteger:
		contacts=paginator.page(1)
	except EmptyPage:
		contacts=Paginator.page(paginator.num_pages)
	return render(request,"guest_manage.html",{"user":username,"guests":contacts})

#@login_required
def search_guest(request):
	username=request.session.get('user','')
	search_phone=request.GET.get("phone","")
	guest_list=Guest.objects.filter(phone__contains=search_phone)
	return render(request,"guest_manage.html",{"user":username,"guests":guest_list})

#@login_required
def sign_index_action(request,event_id):
	event=get_object_or_404(Event,id=event_id)
	phone=request.POST.get('phone','')
	result=Guest.objects.filter(phone=phone)
	if not result:
		return render(request,'sign_index.html',{'event':event,'hint':'phone error.'})
	
	result=Guest.objects.filter(phone=phone,event_id=event_id)
	if not result:
		return render(request,'sign_index.html',{'event':event,'hint':'event id or phone error.'})
	result=Guest.objects.get(phone=phone,event_id=event_id)
	if result.sign:
		return render(request,'sign_index.html',{'event':event,'hint':'user has sign in.'})
	else:
		Guest.objects.filter(phone=phone,event_id=event_id).update(sign='1')
		return render(request,'sign_index.html',{'event':event,'hint':'sign in success!','guest':result})

@login_required
def logout(request):
	auth.logout(request)
	response=HttpResponseRedirect('/index')
	return response
