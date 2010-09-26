from django.shortcuts import render_to_response
import datetime

def hello(request, name):
	current_date = datetime.datetime.now()
	return render_to_response('datetime.html', locals())
