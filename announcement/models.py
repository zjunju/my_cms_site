from django.db import models
from users.models import User

class Announcement(models.Model):
    receiver_choices = (('all','全体教师和学生'), ('all_student','全体学生'),\
                        ('all_teacher','全体教师'),\
                        ('no_thesis_student','未选题学生'), ('thesis_student','已选题学生'))

    sender = models.ForeignKey(User, on_delete = models.CASCADE)
    receiver = models.CharField(max_length=20, choices=receiver_choices)
    text = models.TextField()
    pub_time = models.DateTimeField(auto_now_add = True, verbose_name='发布日期')

    def __str__(self):
        return '<Announcement:%s>'%self.sender

    class Meta:
        verbose_name_plural = '公告栏' 

class Plan(models.Model):
    title = models.CharField(max_length=100,verbose_name='计划标题')
    content = models.TextField(verbose_name='计划详细内容')
    sender = models.ForeignKey(User,on_delete=models.CASCADE,verbose_name='发布者')
    start_time = models.DateField(verbose_name='开始时间')
    stop_time = models.DateField(verbose_name='截至时间')
    person = models.CharField(max_length = 10,choices =(('teacher','教师'),('student','学生')))

    class Meta:
        verbose_name_plural = '计划'
