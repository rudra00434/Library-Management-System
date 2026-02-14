from django.contrib import admin
from .models import Author , Publisher , Book

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Publisher)

# Register your models here.
