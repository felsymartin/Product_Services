from django.shortcuts import render
from django.http import HttpResponse
from .models import product



# Create your views here.

prolist = product.objects.all()



def home(request):
    return render (request,'index.html', {'Pro':prolist})


