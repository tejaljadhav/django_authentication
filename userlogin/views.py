from django.shortcuts import render,HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login
from django.contrib.auth import logout
# Create your views here.
#testuser : admin@123
def home(request):
    #check wheter user is anonymous
    if request.user.is_anonymous:
        return redirect("/login")
    return  render(request,"home.html")
    

def loginuser(request):
    if request.method=="POST":
        print("true")
        username= request.POST.get('username')
        password= request.POST.get('password')
        print("username",username)
        user = authenticate(username=username, password=password)
        if user is not None:
            # a backend authenticated the credentials 
            login(request,user)
            return redirect("/")
        else:
            # no backend authenticated the credentials 
            return render(request,"login.html")
    return render(request,"login.html")

def logoutuser(request):
    logout(request)
    return redirect("/login")   