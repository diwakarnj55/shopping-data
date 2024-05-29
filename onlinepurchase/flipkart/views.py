from django.shortcuts import render
from . models import Purchase

def index(request):
    item=Purchase.objects.all()
    return render(request,"index.html",{"item":item})

