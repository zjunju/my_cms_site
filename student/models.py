from django.db import models
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from schoolinfo.models import StudentInfo
from teacher.models import Teacher
from users.models import User
from thesis.models import Thesis


class Student(StudentInfo):
    introduction = models.TextField(blank = True, null = True, verbose_name = '个人简介')
                                   
    phonenumber = models.CharField(max_length=11 , verbose_name = '手机号码', \
                                    blank = True, null = True)
    email = models.CharField(max_length=30 ,  blank = True, null = True, verbose_name = '邮箱')

    thesis = models.OneToOneField(Thesis, on_delete = models.DO_NOTHING, verbose_name = '论文选题',\
                                blank = True, null = True)

    teacher = models.ForeignKey(Teacher, on_delete = models.DO_NOTHING,verbose_name = '指导老师',\
                                blank = True, null = True)

    user = models.OneToOneField(User, on_delete = models.DO_NOTHING, verbose_name = '用户名',\
                                blank = True, null = True)

    is_choiced_thesis = models.BooleanField(default = False, verbose_name = '是否选题')

    read_announcement = models.ManyToManyField('announcement.Announcement', blank=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = '学生'

class Collection(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)

    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id =  models.PositiveIntegerField()
    content_object = GenericForeignKey('content_type', 'object_id')

    class Meta:
        ordering = ['pk']
        unique_together = (('student','object_id','content_type'))
        verbose_name_plural = '学生收藏选题表'

    def __str__(self):
        return '%s-%s'%(self.student, self.content_object)
