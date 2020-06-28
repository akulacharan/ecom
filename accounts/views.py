from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages



# Create your views here.

def register(request):
    if request.method=='POST':
        username=request.POST['username']
        email = request.POST['email']
        password=request.POST['password']
        re_password=request.POST['re_password']
        if password==re_password:
            if User.objects.filter(username=username).exists():
                messages.info(request,'username-taken')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'email-taken')
            else:
                user=User.objects.create_user(username=username,password=re_password,email=email)
                user.save();
                messages.info(request, 'user-created')
        else:
            messages.info(request, 'password not matched')
        return redirect('login')

    return render(request,'register.html')


def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not  None:
            auth.login(request,user)
            return redirect("/")
        else:
            return redirect('login')
            messages.info(request,'invalid credentials')
    else:
        return render(request,'login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')





