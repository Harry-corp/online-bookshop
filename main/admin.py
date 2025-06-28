from django.contrib import admin
from .models import Book, Category, Author

admin.site.register([Book,Category,Author])