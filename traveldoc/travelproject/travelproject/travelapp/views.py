from django.http import HttpResponse
from django.shortcuts import render
from . models import Place,Team

# Create your views here.
def demo(request):
    obj=Place.objects.all()
    ob=Team.objects.all()

    return render(request,"index.html",{'result':obj,'team':ob})

#def demo1(request):
   # return render(request,"about.html")