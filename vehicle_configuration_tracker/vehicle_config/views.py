from django.http import HttpResponse
from django.shortcuts import render
import datetime

# Create your views here.



def home(request):
    now = datetime.datetime.now()
    html = "<html><body>It is now %s.</body></html>" % now
    return HttpResponse(html)
