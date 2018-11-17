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

    rest_number = models.PositiveIntegerField(default = 0, verbose_name ='剩余指导学生人数')

    collection = GenericRelation('student.Collection')


    def __str__(self):
        return self.name

    def getRestThesisNum(self):
        rest_thesis_num = self.user.thesis_set.filter(is_choiced=False).count()
        return rest_thesis_num
    getRestThesisNum.shor_description = '剩余论文选题数'

    #剩余论文题目集合
    def getRestTheses(self):
        rest_theses = self.user.thesis_set.filter(is_choiced=False)
        return rest_theses

    class Meta:
        verbose_name_plural = '教师'
        ordering = ['-rest_number']
