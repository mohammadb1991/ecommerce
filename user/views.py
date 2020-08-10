from django.shortcuts import render
from django.http import HttpResponse
from .models import user


def sayhello(request):
    return render(request,'hello.html')

# Create your views here.
def see(request):
    users=user.objects.all()
    context={'u':users}
    return render(request,'see.html',context)
def detail(request,id):
    x=user.objects.get(id=id)
    return render(request , 'detail.html',{"detail":x})
