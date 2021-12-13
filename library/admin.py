from django.contrib import admin
from .models.book import Book 
from .models.author import Author   
# Register your models here.
admin.site.register(Book)
admin.site.register(Author)
