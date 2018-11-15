import xadmin
from xadmin.plugins.auth import UserAdmin
from xadmin import views
from users.models import StudentUser, TeacherUser
from thesis.models import Thesis

'''class BaseSettings(object):
    enable_themes = True        #设置admin页面是否出现主题按钮，允许更改页面主题
    use_bootswatch = True       #默认为False，则只有两个主题，如果设置为False，则有很多主题选择'''

class GlobalSettings(object):
    site_title = '大学本科毕业设计管理系统'  #设置网站的title
    site_footer = '玉林师范学院'            #设置网站的footer
    menu_style = 'accordion'               #设置左边的图标样式为折叠

class ThesisInline(object):
    model = Thesis
    extra = 0


class StudentUserAdmin(UserAdmin):
    list_display = ['username']
    def queryset(self):
        qs = super(UserAdmin, self).queryset()
        qs = qs.filter(person='student')
        return qs

class TeacherUserAdmin(UserAdmin):
    inlines = [ThesisInline]
    def queryset(self):
        qs = super(UserAdmin, self).queryset()
        qs = qs.filter(person='teacher')
        return qs

#xadmin.site.register(views.BaseAdminView, BaseSettings)   #注册上面两个设置类
xadmin.site.register(views.CommAdminView, GlobalSettings)
xadmin.site.register(StudentUser, StudentUserAdmin)
xadmin.site.register(TeacherUser, TeacherUserAdmin)
