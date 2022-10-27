from django.shortcuts import render
from django.http import HttpResponse
from CRUD.models import Musician, Album
from CRUD import forms

# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by("first_name")
    diction = {'title':'Home Page', 'musician_list':musician_list}
    return render(request,'CRUD/index.html',context=diction)

def album_list(request, musician_id):
    musician_info = Musician.objects.get(pk=musician_id)
    diction = {'title':'List of Albums', 'musician_info':musician_info}
    return render(request,'CRUD/album_list.html',context=diction)

def musician_form(request):
    form = forms.MusicianForm()

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
    diction = {'title':'Add New Musician', 'musician_form':form}
    return render(request,'CRUD/musician_form.html',context=diction)

def album_form(request):
    form = forms.AlbumForm()

    if request.method == 'POST':
        form = forms.AlbumForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)

    diction = {'title':'Add New Album', 'album_form':form}
    return render(request,'CRUD/album_form.html',context=diction)
