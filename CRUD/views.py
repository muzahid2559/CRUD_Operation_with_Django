from django.shortcuts import render
from django.http import HttpResponse
from CRUD.models import Musician, Album
from CRUD import forms
from django.db.models import Avg

# Create your views here.
def index(request):
    musician_list = Musician.objects.order_by("first_name")

    diction = {'title':'Home Page', 'musician_list':musician_list}
    return render(request,'CRUD/index.html',context=diction)

def album_list(request, musician_id):
    musician_info = Musician.objects.get(pk=musician_id)
    album_list = Album.objects.filter(artist=musician_id).order_by('name','release_date')
    musician_rating_avg = Album.objects.filter(artist=musician_id).aggregate(Avg('num_stars'))

    diction = {'title':'List of Albums', 'musician_info':musician_info, 'album_list':album_list, 'musician_rating_avg':musician_rating_avg}
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

def update_musician(request, musician_id):
    musician_info = Musician.objects.get(pk=musician_id)
    form = forms.MusicianForm(instance=musician_info)

    if request.method == 'POST':
        form = forms.MusicianForm(request.POST, instance=musician_info)

        if form.is_valid():
            form.save(commit=True)
            return album_list(request, musician_id)


    diction = {'update_form':form}
    return render(request, 'CRUD/update_musician.html', context=diction)
