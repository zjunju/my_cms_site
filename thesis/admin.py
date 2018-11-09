from django.contrib import admin
from .models import Thesis, Tag

@admin.register(Thesis)
class ThesisAdmin(admin.ModelAdmin):
    list_display = ['pk','title', 'pub_date', 'publisher', 'is_choiced', 'student']

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ['name']