from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Message
def hello_world(request):
    msgs=Message.objects.all()
    name = request.user.username
    return render(request,'msg.html',{'key':name,'msgs':msgs})