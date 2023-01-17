from django.contrib import admin

from CRUD.models import Album, Musician

# Register your models here.
admin.site.register(Musician)
admin.site.register(Album)



admin.site.site_header = "CRUD Admin"
admin.site.site_title = "CRUD Admin Portal"
admin.site.index_title = "Welcome to CRUD Admin Portal"
