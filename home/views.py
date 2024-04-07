from django.shortcuts import render
from django.http import HttpResponse

def home(request):

    content = "Interchange App Test again"
    return HttpResponse(content, content_type="text/plain")
