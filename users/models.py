from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    person = models.CharField(max_length = 10, blank=True, null=True, verbose_name='人物',
                                choices = (('teacher','教师'), ('student', '学生')))
    no_r_message_count = models.PositiveIntegerField(default=0)
    no_r_ann_count = models.PositiveIntegerField(default=0)

    def __str__(self):
        if self.person == 'teacher':
            return '%s'%self.teacher.name
        elif self.person == 'student':
            return '%s'%self.student.name
        else:
            return self.username

    def get_person_name(self):
        if self.person == 'teacher':
            return '%s'%self.teacher.name
        elif self.person == 'student':
            return '%s'%self.student.name
        else:
            return self.username
    get_person_name.short_description = '用户姓名'

    class Meta:
        ordering = ['pk']
        verbose_name = '用户表'
        verbose_name_plural = verbose_name


class StudentUser(User):
    class Meta:
        verbose_name = '学生用户表'
        verbose_name_plural = verbose_name
        proxy = True  #将另一个模型子类化的模型视为代理模型。proxy = True,不为改模型创建表

class TeacherUser(User):
    class Meta:
        verbose_name = '教师用户表'
        verbose_name_plural = verbose_name
        proxy = True
