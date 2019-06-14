from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import json
from .models import *
import os, sys

# Create your views here.

def example_get(request, var_a, var_b): #this must be the same name as in the functions in the url
	try:#this is the debug set
		returnob = {
		"data": "Pizza is lyfe %s: aaaaand Tacos %s" %(var_a, var_b),
		}
		return JsonResponse(returnob)
	except Exception as e:
		exc_type, exc_obj, exc_tb = sys.exc_info()
		other = sys.exc_info()[0].__name__
		fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
		errorType = str(exc_type)
		return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})

@csrf_exempt #this is a decorator that modifys the function
def example_post(request):
	log = []
	if request.method == "POST":
		try:
			data = request.POST["data"]
			jsob = json.loads(data)

			index = 0
			for i in jsob["demo"]:
				index += 1
				# index = index + 1

			return JsonResponse({"Count":index})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		return HttpResponse("<h1>ONLY POST REQUESTS</h1>")


@csrf_exempt #this is a decorator that modifys the function
def fib(request):
	jsob = {"startNumber": 0, "length": 10}
	log = [] #this is used to print errors if there are problems
	if request.method == "POST":
		try:
			data = request.POST["data"]
			received = json.loads(data)
			jsob = json.loads(data)
			###############################################
			##Everything above this line is always required
			###############################################
			startNumber = int(jsob["startNumber"])
			length = int(jsob["length"])
			loop = range(length)

			numarray = []
			fibno = startNumber
			addno = 1
			for l in loop:
				numarray.append(fibno)
				fibno = fibno + addno
				addno = fibno - addno

			#return JsonResponse({"Count":index})
			return JsonResponse({"fib":numarray})
		except Exception as e:
			exc_type, exc_obj, exc_tb = sys.exc_info()
			other = sys.exc_info()[0].__name__
			fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
			errorType = str(exc_type)
			return JsonResponse({"isError": True, "error":str(e), "errorType":errorType, "function":fname, "line":exc_tb.tb_lineno, "log":log})
	else:
		#return HttpResponse("<h1>ONLY POST REQUESTS</h1>")
		return JsonResponse(jsob)
