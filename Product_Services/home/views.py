from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import product
from django.db.models.query_utils import Q

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



