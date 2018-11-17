"""cms_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
import xadmin
from django.urls import path, include
from users import views
from .views import download_file, delete_file, upload_file
                    
urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path(r'captcha', include('captcha.urls')),  # 验证码

    #users.view
    path('', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('update_password/', views.update_password, name='update_password'),

    path('upload/', upload_file, name='upload_file'),
    path('delete/', delete_file, name='delete_file'),
    path('download', download_file, name='download_file'),
    path('teacher/', include('teacher.urls')),
    path('student/', include('student.urls')),
    path('thesis/', include('thesis.urls')),
]
