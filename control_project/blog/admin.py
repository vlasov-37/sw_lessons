from django.contrib import admin
from .models import Author, Record, Tag

admin.site.register(Author)
admin.site.register(Record)
admin.site.register(Tag)
