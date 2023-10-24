from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

def user_signup(request):
    if request.method == 'POST':
        un = request.POST.get('un')
        pw1= request.POST.get('pw1')
        pw2= request.POST.get('pw2')
        if pw1 == pw2:
            try:
                user = User.objects.get(username=un)
                return render(request,"user_signup.html",{"msg":"Username already exists"})
            except User.DoesNotExist:
                usr = User.objects.create_user(username=un,password=pw1)
                usr.save()
                return redirect("user_login")
        else:
            return render(request,"user_signup.html",{"msg":"Passwords do not match"})
    else:
        return render(request,"user_signup.html")
    
def user_login(request):
    if request.method == "POST":
        un = request.POST.get('un')
        pw = request.POST.get('pw')
        user = authenticate(username=un,password=pw)
        if user is not None:
            login(request,user)
            return redirect("home")
        else:
            return render(request,"user_login.html",{"msg":"Invalid Credentials"})
    else:
    	return render(request,"user_login.html")

def user_logout(request):
	logout(request)
	return redirect("landing")

def landing(request):
    return render(request,"landing.html")

def contact(request):
    return render(request,"contact.html")
    
                
