from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Message
from .forms import MessageForm

def hello_world(request):
    if(request.method=='GET'):
        #request.GET
        form=MessageForm()
        msgs=Message.objects.all()
        name = request.user.username
        return render(request,'msg.html',{'key':name,'form':form,'msgs':msgs})
    elif(request.method=='POST'):
        #request.POST
        text=request.POST.get('text')
        Message.objects.create(text=text)
        form=MessageForm()
        msgs=Message.objects.all()
        name = request.user.username
        return render(request,'msg.html',{'key':name,'form':form,'msgs':msgs,'rec':True})

class MessageView(View):
    def get(self,request):
        form=MessageForm()
        msgs=Message.objects.all()
        name = request.user.username
        return render(request,'msg.html',{'key':name,'form':form,'msgs':msgs})
    
    def post(self,request):
        text=request.POST.get('text')
        Message.objects.create(text=text)
        form=MessageForm()
        msgs=Message.objects.all()
        name = request.user.username
        return render(request,'msg.html',{'key':name,'form':form,'msgs':msgs,'rec':True})
