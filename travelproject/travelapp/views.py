from django.http import HttpResponse
from django.shortcuts import render
from .models import Place
from .models import Team


def demo(request):
    obj=Place.objects.all()
    obj1=Team.objects.all()
    return render(request, "index.html",{'result':obj,'result2':obj1})
# def operations(request):
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     res=x+y
#
#     x=int(request.GET['num1'])
#     y=int(request.GET['num2'])
#     sub=x-y
#
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     mul = x * y
#
#     x = int(request.GET['num1'])
#     y = int(request.GET['num2'])
#     div = x / y
#
#     return render(request,"result.html",{'result':res,'subt':sub,'mult':mul,'divis':div})