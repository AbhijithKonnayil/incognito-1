from django.http.response import HttpResponse
from django.shortcuts import render
from django.views import View
from .models import Message
from .forms import MessageForm
from django.contrib.auth.models import Permission, User
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
    
    def get(self,request,username):
        if(request.user.is_authenticated):
            form=MessageForm()
            msgs=Message.objects.filter(user=request.user)
            name = request.user.username
            return render(request,'msg.html',{'key':name,'form':form,'msgs':msgs})
        raise PermissionError('Permission Denied')
    def post(self,request,username):
        print(username)
        text=request.POST.get('text')
        user = User.objects.get(username=username)
        Message.objects.create(text=text,user=user)
        form=MessageForm()
        msgs=Message.objects.filter(user=request.user)
        name = request.user.username
        return render(request,'msg.html',{'key':name,'form':form,'msgs':msgs,'rec':True})

#MessageSend
#
