from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    diction = {'title':'Home Page'}
    return render(request,'CRUD/index.html',context=diction)

def album_list(request):
    diction = {'title':'List of Albums'}
    return render(request,'CRUD/album_list.html',context=diction)

def musician_form(request):
    diction = {'title':'Add New Musician'}
    return render(request,'CRUD/musician_form.html',context=diction)

def album_form(request):
    diction = {'title':'Add New Album'}
    return render(request,'CRUD/album_form.html',context=diction)
