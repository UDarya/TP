from django.shortcuts import render

#from django.http import HttpResponse
#from urlparse import parse_qs

def index(request):
		return render(request, 'index.html') 

def login(request):
		return render(request, 'login.html')	

def signup(request):
		return render(request, 'signup.html')

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