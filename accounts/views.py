from django.shortcuts import render,redirect

# from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django.views.generic import View
from django.contrib.auth.views import LoginView,PasswordChangeView
from .forms import sigup
# Create your views here.


# def signUp(request):
#     form = sigup()
#     if request.method == "POST":
#         form = sigup(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request,user)
#             return redirect('home')
#     return render(request,"signup.html",{"signup":form})


# class signUp(View):
#     def post(self,request):
#         form = sigup(request.POST)
#         if form.is_valid():
#             user = form.save()
#             auth_login(request,user)
#             return redirect('home')
#         return render(request,"signup.html",{"signup":form})


class signUp(CreateView):
    model = auth_login
    form_class = sigup
    template_name = "signup.html"
    success_url = '/login'



class Login(LoginView):
    template_name = "login.html"
    success_url = '/home'



class ChangePassword(PasswordChangeView):
    template_name ="changepassword.html"
    success_url = '/login'