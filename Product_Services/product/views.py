from django.shortcuts import render
from home.models import product


# Create your views here.

def productdetails(request):

    pro_id = request.GET['id']
    obj_id = product.objects.get(id=pro_id)
    return render(request,'product.html',{'objid':obj_id})
