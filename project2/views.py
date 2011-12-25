# coding=UTF-8
import os, sys
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render_to_response
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from project2.mymod.models import *


def hello_page(request):
	return render_to_response('base.html')

def red(request):
	return HttpResponseRedirect('http://127.0.0.1:8000/')

@login_required	
def profile(request):

	q=Group.objects.filter(students__first_name=request.user.first_name, students__last_name=request.user.last_name)
	group="%s" % q
	subjects="<p>"
	q=DE.objects.filter(student__first_name=request.user.first_name, student__last_name=request.user.last_name)
	for i in q:
		subjects+="<u>%s</u><br>" % i
		w=Lecture.objects.filter(de__student__first_name=request.user.first_name, de__student__last_name=request.user.last_name, de__tema__name="%s" % i)
		for j in w:
			subjects+="  %s " % j
			if j.is_read:
				subjects+="is readed<br>"
			else:
				subjects+="unreaded<br>"
		subjects+="<br>"
		w=Practice.objects.filter(de__student__first_name=request.user.first_name, de__student__last_name=request.user.last_name, de__tema__name="%s" % i)
		for j in w:
			subjects+="  %s " % j
			if j.is_done:
				subjects+="is done<br>"
			else:
				subjects+="undone<br>"
		subjects+="<br>"
		w=TestResult.objects.filter(de__student__first_name=request.user.first_name, de__student__last_name=request.user.last_name, de__tema__name="%s" % i)
		for j in w:
			subjects+="%s <br>" % j
		subjects+="<br><br>"

			
	subjects+="</p>"
	c = {
		'name' : request.user.get_full_name(), 
		'last_time' : request.user.last_login,
		'status' : request.user.is_staff,
		'group' : group,
		'subjects' : subjects
		}
	return render_to_response('profile.html', c)
	
@login_required
def lecture_view(request, lecture_name, lecture_page):
	q=Lecture.objects.filter(de__student__first_name=request.user.first_name, de__student__last_name=request.user.last_name, name="%s" % lecture_name)
	for i in q:
		if not i.is_read:
			i.is_read=True
			i.save()
	return render_to_response('lecture.html',{'lecture_name' : lecture_name, 'lecture_page' : lecture_page})
	
@login_required
def practice_view(request, practice_name, practice_page):
	q=Practice.objects.filter(de__student__first_name=request.user.first_name, de__student__last_name=request.user.last_name, name="%s" % practice_name)
	for i in q:
		if not i.is_done:
			i.is_done=True
			i.save()
	return render_to_response('practice.html',{'practice_name' : practice_name, 'practice_page' : practice_page})
	
@login_required
def test_view(request,test_name,test_id, tema):
	questions=""
	a=0
	q=Question.objects.filter(test__test_id=test_id)
	for i in q:
		a+=1
		questions+="<p>%s</p>" % i.text
		questions+="<input type=\"text\" name=\"answer%i\" value=\"\" id=\"answer%i\"> <br> <br>" % (a,a)
	
	questions+="<input type=\"submit\" value=\"Finish\" />"
	return render_to_response('test.html', {'test_name' : test_name, 'test_id' : test_id, 'questions' : questions})

@login_required
def test_result(request, test_id):
	if request.method == 'POST':
		q=Question.objects.filter(test__test_id=test_id)
		a=0
		k=0.0
		for i in q:
			a+=1
			if i.answer == request.POST['answer%i' % a]:
				k+=1.0
		q=TestResult.objects.get(de__student__first_name=request.user.first_name,de__student__last_name=request.user.last_name,test_id=test_id)
		q.result=int(k/a*3)+2
		q.save()
		return HttpResponseRedirect('http://127.0.0.1:8000/accounts/profile/')
	else:
		return HttpResponseRedirect('http://127.0.0.1:8000/accounts/profile/')
			
			
