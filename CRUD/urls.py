from django.urls import path
from CRUD import views


app_name = "CRUD"


urlpatterns = [

    path('', views.index, name='index'),
    path('add_musician/', views.musician_form, name='musician_form'),
    path('add_album/', views.album_form, name='album_form'),
    path('album_list/<int:musician_id>/', views.album_list, name='album_list'),
    path('update_musician/<int:musician_id>/', views.update_musician, name='update_musician'),
]
