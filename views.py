from django.http import HttpResponse
import datetime


def hello(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404()
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<h1>In %s hour(s), it will be %s.</h1>" % (offset, dt)
	return HttpResponse(html)
