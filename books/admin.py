from django.contrib import admin
from pyweb.books.models import *

admin.site.register(Publisher)
admin.site.register(Author)
admin.site.register(Book)
