from django.shortcuts import render,redirect
from home.models import product,comment


# Create your views here.

def productdetails(request):

    pro_id = request.GET['id']
    obj_id = product.objects.get(id=pro_id)
    return render(request,'product.html',{'objid':obj_id})

def commenttext(request):    

    text = request.GET['txt']
    pro_id = request.GET['productid']
    username = request.GET['username']
    obj_id = product.objects.get(id=pro_id)

    cmt = comment.objects.create (name = username, product = obj_id, body = text)
    cmt.save();
        
    #return render(request,'product.html',{'objid':obj_id})
    return redirect('/details/?id='+pro_id)


