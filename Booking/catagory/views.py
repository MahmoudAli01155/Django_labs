from django.shortcuts import render
from django.http.response import HttpResponse, HttpResponseRedirect
from .models import *
# Create your views here.

# view method(httprequest)--->return HttpResponse


def List(r):
    context = {}
    context['username'] = 'Asd@yahoo.com'
    return render(r, 'index.html', context)


def Add(req):
    if(req.method=='GET'):
        return  render(req,'catagory/Add.html')
    else:
        data=req.POST
        print(data['catgoryname'])
        catobj = Catagory()
        Catagory.objects.create(name=req.POST['catgoryname'])

        # catobj=Catagory()
        catobj.name=data['catgoryname']
        catobj.save()

        # insert in db
        context={}
        context['msg']='added'
        return render(req, 'catagory/Add.html',context)


def Update(req,catid):
    context = {}
    if(req.method=='GET'):
        #get catagory object from db
        #select * from catatgory_catagory where id=catid
        cat=Catagory.objects.get(id=catid)
        context['cat']=cat
        return render(req,'catagory/Update.html',context)
    else:
        Catagory.objects.filter(id=catid).update(name=req.POST['catgoryname'])
        #context['catagories']=Catagory.objects.all()
        #return render(req, 'catagory/index.html',context)
        return HttpResponseRedirect('/')
