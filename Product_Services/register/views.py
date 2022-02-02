from django.shortcuts import render


# Create your views here.
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def validate(request):
    uname=request.GET['uname']
    psw=request.GET['psw']
    if uname=='felsy' and psw=='felsy@123':

        return render(request,'success.html')
    else:
        return render(request,'invalid.html')
