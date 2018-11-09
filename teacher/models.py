from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from schoolinfo.models import TeacherInfo
from users.models import User


class Teacher(TeacherInfo):
    introduction = models.TextField(blank = True, null = True, verbose_name = '个人简介')

    phonenumber = models.CharField(max_length=11 , verbose_name = '手机号码',\
                                    blank = True, null = True)

    email = models.CharField(max_length=30, blank = True, null = True,\
                             verbose_name = '邮箱')

    user = models.OneToOneField(User, on_delete = models.CASCADE, verbose_name = '用户名',\
                                blank = True, null = True,)

    max_number = models.PositiveIntegerField(default = 0, verbose_name = '最大指导学生人数')

    collection = GenericRelation('student.Collection')

    read_announcement = models.ManyToManyField('announcement.Announcement', blank=True)

    

    def __str__(self):
        return self.name

    def getRestNumber(self):
        rest_number = self.max_number - self.student_set.count()
        return rest_number
    getRestNumber.short_description = '剩余指导人数'


    def getRestThesisNum(self):
        rest_thesis_num = self.user.thesis_set.filter(is_choiced=False).count()
        return rest_thesis_num
    getRestThesisNum.shor_description = '剩余论文选题数'

    def getRestTheses(self):
        rest_theses = self.user.thesis_set.filter(is_choiced=False)
        return rest_theses

    class Meta:
        verbose_name_plural = '教师'
        ordering = ['pk']
