from .models import Student
import xadmin

class StudentAdmin(object):
    list_display = ['number', 'name', 'class_name', 'college', 'is_choiced_thesis','phonenumber', 'email']
    list_filter = ['number', 'name', 'class_name', 'college', 'is_choiced_thesis']
    search_fields = ['number', 'name', 'class_name', 'college', 'is_choiced_thesis']
    exclude = ['user']      #不显示的字段
    readonly_fields = ['number', 'name', 'class_name']  #只读字段，不能修改
    model_icon = 'fa fa-user-circle-o'      #设置图标
    list_editable = ['phonenumber', 'email']

xadmin.site.register(Student, StudentAdmin)
