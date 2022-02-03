from django.shortcuts import render
from django.contrib.auth.models import User


# Create your views here.
def login(request):
    return render(request,'login.html')#For  login Purpose

def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        npsw=request.POST['npsw']
        rpsw=request.POST['rpsw']
        if npsw==rpsw:
            if User.objects.filter(username=uname).exists():
                umsg="The username already exists!!!"
                return render(request,'register.html',{'umsg':umsg})
            elif User.objects.filter(email=email).exists():
                emsg="Email-Id already taken"
                return render(request,'register.html',{'emsg':emsg})
            else:           
            
                user= User.objects.create_user(username=uname,first_name=fname,last_name=lname,password=npsw,email=email)
                user.save();
                return render(request,'success.html')
        else:
            pmsg="Password doesn't match!!!"
            return render(request,'register.html',{'pmsg':pmsg})

    else:

        return render(request,'register.html')# For registration

def validate(request): # To validate login process
    uname=request.POST['uname']
    psw=request.POST['psw']
    if uname=='felsy' and psw=='felsy@123':

        return render(request,'success.html')
    else:
        return render(request,'invalid.html')


    
