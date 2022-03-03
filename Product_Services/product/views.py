from django.shortcuts import render,redirect
from home.models import product,comment
from django.core.cache import cache


# This productdetails function for cache work only!
def productdetails(request):

    pro_id = request.GET['id']
    if cache.get(pro_id):
        print ("###### Data from cache ########")
        obj_id = cache.get(pro_id)

    else:
        print ('##### Data from DAtaBAse#####')
        obj_id = product.objects.get(id=pro_id)
        cache.set(pro_id,obj_id)
    return render(request,'product.html',{'objid':obj_id})

# This productid details for session work coding

def productdetails_2(request,pageid):
    
    obj_id = product.objects.get(id=pageid)
    if 'recent_view' in request.session:                
        if pageid in request.session['recent_view']:

            request.session['recent_view'].remove (pageid)
        previous = product.objects.filter(id__in= request.session['recent_view'])
        print("Previous view:",previous)
        request.session['recent_view'].insert(0,pageid)
        # To limit the length of product in list
        if len(request.session['recent_view'])>4:
            request.session['recent_view'].pop()

    else:
        previous = [1]
        request.session['recent_view'] = [pageid]
    request.session.modified = True
    print("Show Id",request.session['recent_view'])

    return render(request,'product.html',{'objid':obj_id,'prev':previous})

#This function is for giving comment
def commenttext(request):    

    text = request.GET['txt']
    pro_id = request.GET['productid']
    username = request.GET['username']
    obj_id = product.objects.get(id=pro_id)

    cmt = comment.objects.create (name = username, product = obj_id, body = text)
    cmt.save();
        
    #return render(request,'product.html',{'objid':obj_id})
    #return redirect('/details/?id='+pro_id)
    return redirect('/details/'+pro_id)


