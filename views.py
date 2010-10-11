from django.shortcuts import render_to_response
import datetime

def hello(request, name):
	current_date = datetime.datetime.now()
	return render_to_response('datetime.html', locals())

def meta(request):
	values = request.META.items()
	values.sort()
	return render_to_response('metalist.html', {'request_meta':values})

