from django.shortcuts import render, HttpResponse, redirect
from .models import *


def index(request):
    
    context = {
        
        "all_dojos": Dojo.objects.all(),
        "all_ninjas": Ninja.objects.all(),
        
        
    }
    return render(request, "index.html", context)

def add_dojo(request):
    Dojo.objects.create(
        name=request.POST['name'],
        city=request.POST['city'],
        state=request.POST['state'],
    )
    return redirect('/')



def add_ninja(request):
    Ninja.objects.create(
        dojo = Dojo.objects.get(id=int(request.POST["from_dojo"])),
        first_name=request.POST['first_name'],
        last_name=request.POST['last_name'],
    )
    return redirect('/')


def delete_ninja(request, ninja_id):
    ninja = Ninja.objects.get(id=ninja_id)
    ninja.delete()
    return redirect('/')


def delete_dojo(request, dojo_id):
    del_dojo = Dojo.objects.get(id=dojo_id)
    del_dojo.delete()
    return redirect('/')








