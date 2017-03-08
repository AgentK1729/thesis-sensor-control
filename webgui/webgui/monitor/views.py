from django.shortcuts import render
from django.http import HttpResponse
from monitor import *

def home(request):
	request.session['count'] = request.session.get("count", -1) + 1
	index = request.session.get("index", 0)
	if request.session['count'] % 20 == 0 and request.session['count'] > 0:
		request.session['map'] = init_map()
		monitor_out = monitor(request.session['map'], index)
		request.session['index'] = monitor_out[2]
	else:
		if request.session['count'] == 0:
			request.session['map'] = init_map()
		monitor_out = monitor(request.session['map'], index)
		request.session['index'] = monitor_out[2]
		request.session['map'] = request.session.get("map", monitor_out[0])
	return render(request, "home.html", {"map":monitor_out[0], "green":monitor_out[1][0],
		"red":monitor_out[1][1], "yellow":monitor_out[1][2], "index":index})

def stop(request):
	del request.session['map']
	del request.session['index']
	del request.session['count']
	return HttpResponse("Aborted")