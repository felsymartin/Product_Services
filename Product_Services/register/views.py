from pydoc import resolve
from django.shortcuts import redirect, render
from django.contrib.auth.models import User,auth

#Register Email
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def login(request):
    if request.method=='POST':
        uname=request.POST['uname']
        psw=request.POST['psw']
        user = auth.authenticate(username=uname,password=psw)
        if user is not None:
            #Login action
            auth.login(request,user)

            #Adding cookies
            response = redirect('/')

            response.set_cookie('uname',uname)
            response.set_cookie('Login',True)
            #End cookies
            return response
        else:
            lmsg='Invalid username or password!!!'
            return render(request,'login.html',{'lmsg':lmsg})   
              
    else:
        return render(request,'login.html')#For  login Purpose

otp = '5555'
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
                response = render(request,'otp.html')#Load otp page

                response.set_cookie('uname1',uname)            
                response.set_cookie('fname',fname)
                response.set_cookie('lname',lname)
                response.set_cookie('password',npsw)
                response.set_cookie('email',email)                

                subject = 'Product Services -OTP for Registration'
                mailmsg = f''' Hi {uname} ,
                Please use the below OTP to complete registration.
                OTP : {otp} '''                
                email_from = settings.EMAIL_HOST_USER
                send_mail(subject,mailmsg,email_from,[email])

                return response
                
        else:
            pmsg="Password doesn't match!!!"
            return render(request,'register.html',{'pmsg':pmsg})

    else:
        return render(request,'register.html')# For registration

def register_valid(request):
    
    code = request.POST['emailcode']
    if code == otp:
        #if 'uname' in request.COOKIES:

        uname1 = request.COOKIES['uname1']       
        fname1 = request.COOKIES['fname']       
        lname1 = request.COOKIES['lname']       
        npsw1 = request.COOKIES['password']       
        email1 = request.COOKIES['email']       

        user= User.objects.create_user(username=uname1,first_name=fname1,last_name=lname1,password=npsw1,email=email1)
        user.save();
        auth.login(request,user)
        return redirect('/')

    else:
        otpmsg="OTP is INVALID!!!"

        return render(request,'otp.html',{'otpmsg':otpmsg})

def logout(request):
    auth.logout(request)

    #delete cookies
    response = redirect('/')
    response.delete_cookie('uname')
    response.delete_cookie('Login')

    return response





    
