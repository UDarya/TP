from django.shortcuts import render
from django.db import models
from aplic.models import Profile, Tag, Question, Answer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count

#from django.http import HttpResponse
#from urlparse import parse_qs

def index(request):
		q = Question.objects.all().prefetch_related('tags','author').order_by('-date_added').annotate(Count('answer'))
		paginator = Paginator(q,20)
		page = request.GET.get('page')
		try:
				p = paginator.page(page)
		except PageNotAnInteger:
				p = paginator.page(1)
		except EmptyPage:
				p = paginator.page(paginator.num_pages)
		return render(request, 'index.html',{"questions":p}) 

def sort(request):
		q = Question.objects.all().prefetch_related('tags','author').order_by('-author__rating').annotate(Count('answer'))
		paginator = Paginator(q,20)
		page = request.GET.get('page')
		try:
				p = paginator.page(page)
		except PageNotAnInteger:
				p = paginator.page(1)
		except EmptyPage:
				p = paginator.page(paginator.num_pages)
		return render(request, 'index.html',{"questions":p}) 

def login(request):
		return render(request, 'login.html')	

def signup(request):
		return render(request, 'signup.html')

def answer(request, q_id):
		q = Question.objects.prefetch_related('tags','author').get(id = q_id)
		a = Answer.objects.select_related('author').filter(question_id=q_id).order_by('-date_added')
		return render(request, 'answers.html', {"q_ans":q, "answers":a})


#	output = '<br>'+'GET:'	
#		for val in request.GET:
#			output += '<br>' + val + ' = ' + request.GET[val]
#
#		output += '<br>'+'POST:'
#
#		for value in request.POST:
#			output += value + request.POST[value]
#
#		return HttpResponse(output)