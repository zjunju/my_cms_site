from django.urls import path, include
from . import views
from .student_thesis_views import student_thesis,teacher_list, thesis_list,\
                                  thesis_list_with_tag, teacher_info, \
                                  cancel_thesis,apply_thesis, apply_teacher,cancel_teacher,\
                                  add_thesis, delete_thesis
from .student_collection_views import collect, cancel_collect, student_collection

urlpatterns = [
    path('', views.student_home, name = 'student_home'),
    path('update_info/', views.student_update_info, name='student_update_info'),  #学生更新信息
    
    path('message/', include([ 
        path('', views.student_message, name='student_message'),
        path('send/', views.student_send_message, name='student_send_message'),
        path('no_read', views.student_no_read_message, name='student_no_read_message'),
        ]),
    ), 

    path('announcement/', include([
            path('all/', views.all_announcement, name='all_announcement'),
            path('<int:announcement_pk>', views.announcement_detail, name='announcement_detail'),
        ])),
    
    path('collect/<int:object_id>', collect, name='collect'),    #学生收藏教师或论文题目
    path('collection', student_collection, name='student_collection'),   #学生的收藏
    path('collection/cancel_collect', cancel_collect, name='cancel_collect'),  #取消收藏

    path('teacher_list/', teacher_list, name='teacher_list'),         #教师列表
    path('teacher_info/', teacher_info, name='teacher_info'),     #查看教师信息
    path('apply_teacher/<int:teacher_pk>', apply_teacher, name='apply_teacher'),
    path('cancel_teacher/', cancel_teacher, name='cancel_teacher'),

    path('thesis/', include([
         path('', student_thesis, name = 'student_thesis'),
         path('thesis_list', thesis_list, name='thesis_list'),
         path('tag/<str:tag_name>', thesis_list_with_tag, name='thesis_list_with_tag'),
         path('<int:thesis_pk>/apply', apply_thesis, name='apply_thesis'),
         path('<int:thesis_pk>/cancel', cancel_thesis, name='cancel_thesis'),
         path('add_thesis', add_thesis, name='add_thesis'),
         path('delete_thesis/<int:thesis_pk>', delete_thesis, name='student_delete_thesis'),
        ]),
        ),  
]

