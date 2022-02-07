from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.

pro1 = models.product()
pro1.name='Watch'
pro1.image='1.jpg'

pro2 = models.product()
pro2.name='Shoes'
pro2.image='2.jpg'

pro3 = models.product()
pro3.name='Ipods'
pro3.image='3.jpg'

pro4 = models.product()
pro4.name='Bottle'
pro4.image='4.jpg'

prolist=[pro1,pro2,pro3,pro4]

def home(request):
    return render (request,'index.html', {'Pro':prolist})


