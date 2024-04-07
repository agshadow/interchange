from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    content = "Interchange App"
    return HttpResponse(content, content_type="text/plain")
