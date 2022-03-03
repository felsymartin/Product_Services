from django.shortcuts import redirect, render
from django.http import HttpResponse, JsonResponse
from .models import product
from django.db.models.query_utils import Q
from django.conf import settings
from django.core.mail import send_mail

# Create your views here.
def home(request):
    if request.method == 'POST':
        value = request.POST['search']
        proli = product.objects.filter(name__istartswith  = value)
        return render (request, 'index.html', {'Pro': proli} )
    else:
        prolist = product.objects.all()
        if 'uname' in request.COOKIES:
            sendjinja = {
                'Pro':prolist,
                'username':request.COOKIES['uname'],
                'login':request.COOKIES['Login']
            }

            return render (request,'index.html', sendjinja)
        else:
        
            return render (request,'index.html', {'Pro':prolist})       


# Function for search autocomplete
def search(request):
    prolist = product.objects.all()
    
    if 'term' in request.GET:
        name = request.GET['term']
        print(name)
        numlist = []
        objlist = product.objects.filter(Q(name__istartswith = name))
        for i in objlist:
            numlist.append(i.name)
        
        return JsonResponse (numlist, safe = False)

    return render (request,'index.html', {'Pro':prolist})

def email(request):
    name = request.POST['name']
    mail = request.POST['email']
    phone = request.POST['phone']
    msg = request.POST['message']
    support_email = ['felsydjango@gmail.com']
    subject = 'Customer support from Product Services'
    mailmsg = f'''Hi Felsy. I like to inform that Mr/Ms {name} given a contact message.
    The message was {msg}

    email: {mail}
    phone no: {phone}
    ''' 
    email_form = settings.EMAIL_HOST_USER
    send_mail(subject,mailmsg,email_form,support_email)

    return redirect('/')




