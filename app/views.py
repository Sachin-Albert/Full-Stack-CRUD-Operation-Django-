from django.shortcuts import render,redirect
from .models import createdata
from django.http import HttpResponse

def index(request):
    data = createdata.objects.all()
    return render (request,'index.html',{'datas':data})
   

def create(request):
    if request.method == 'POST':
        uname = request.POST.get('name')
        uphone = request.POST.get('phone')
        upara = request.POST.get('para')
        data = createdata.objects.create(name=uname,phone=uphone,para=upara)
        data.save()
        return redirect('/')
    return render(request,'create.html')

def read(request,id):
    data = createdata.objects.get(id=id)
    data.save()
    return render(request,'read.html',{'datas':data})

def update(request,id):
    data = createdata.objects.get(id=id)
    if request.method=='POST':
        data.name = request.POST.get('name')
        data.phone = request.POST.get('phone')
        data.para = request.POST.get('para')
        data.save()
        return redirect('/')
    return render (request,'update.html',{'datas':data})

def deleteitem(request,id):
    data = createdata.objects.get(id=id)
    data.delete()
    return redirect('/')
