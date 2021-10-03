from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View

def hello_world(request):
    print(request.method)
    name = 'Shibin'
    return render(request,'msg.html',{'key':name})