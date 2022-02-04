from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth


# Create your views here.
def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        psw=request.POST['psw']
        user = auth.authenticate(username=uname,password=psw)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            lmsg='Invalid username or password!!!'
            return render(request,'login.html',{'lmsg':lmsg})       
             

    else:
        return render(request,'login.html')#For  login Purpose

def register(request):
    if request.method=='POST':
        fname=request.POST['fname']
        lname=request.POST['lname']
        uname=request.POST['uname']
        email=request.POST['email']
        npsw=request.POST['npsw']
        rpsw=request.POST['rpsw']
        #checking the password condition & render the page on if the password matches
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
                auth.login(request,user)
                return redirect('/')
        else:
            pmsg="Password doesn't match!!!"
            return render(request,'register.html',{'pmsg':pmsg})

    else:

        return render(request,'register.html')# For registration


def logout(request):
    auth.logout(request)
    return redirect('/')



    
