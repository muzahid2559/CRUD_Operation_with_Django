from django.urls import path
from CRUD import views


app_name = "CRUD"


urlpatterns = [

    path('', views.index, name='index'),
    path('add_musician/', views.musician_form, name='musician_form'),
    path('add_album/', views.album_form, name='album_form'),
]
