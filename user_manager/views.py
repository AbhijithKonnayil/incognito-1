from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views import View
from user_manager.forms import LoginForm
from django.contrib.auth import authenticate, login, logout

class LoginView(View):
    def post(self,request):
        print(request.POST)
        form=LoginForm(request.POST)
        #print(form)
        if(form.is_valid()):
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            print("user - ",user)
            if(user):
                login(request, user)
                print(request.user)
                return HttpResponseRedirect('/msg/')
            else:
                return render(request, 'login.html', {'form':form,'error':'Invalid Credentials'})   
        else:
            return render(request, 'login.html', {'form':form})   

    def get(self, request):
        form = LoginForm()
        return render(request, 'login.html', {'form':form}) 

class LogoutView(View):
    def get(self,request):
        logout(request)
        return HttpResponseRedirect('/login')