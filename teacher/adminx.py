import xadmin
from .models import Teacher
from thesis.models import Thesis

class TeacherAdmin(object):
    list_display = ['number', 'name', 'college', 'user', 'rest_number']
    list_filter = ['number', 'name', 'college']
    search_fields = ['number', 'name', 'college']
    model_icon = 'fa fa-user-circle'
    refresh_times = [3,5]

xadmin.site.register(Teacher, TeacherAdmin)
