import xadmin
from .models import Tag, Thesis

class ThesisAdmin(object):
    list_display = ['title', 'pub_date', 'publisher', 'is_choiced', 'tags', 'getCollege']
    list_filter = ['title', 'pub_date', 'is_choiced', 'tags', 'publisher__teacher__college']
    search_fields =['title',  'publisher__teacher__name']
    model_icon = 'fa fa-book'

class TagAdmin(object):
    list_display = ['name']
    list_filter = ['name']
    search_fields = ['name']
    model_icon = 'fa fa-tags'


xadmin.site.register(Thesis, ThesisAdmin)
xadmin.site.register(Tag, TagAdmin)
