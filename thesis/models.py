from django.db import models
from django.contrib.contenttypes.fields import GenericRelation
from ckeditor.fields import RichTextField

class Tag(models.Model):
    name = models.CharField(max_length = 50, verbose_name='标签名')

    def __str__(self):
        return '%s'%self.name

    class Meta:
        verbose_name_plural = '论文标签'

class Thesis(models.Model):
    title = models.CharField(max_length = 255, verbose_name='论文题目')
    content = RichTextField(default='', verbose_name='选题内容')
    pub_date = models.DateField(auto_now_add = True, verbose_name='发布日期')
    publisher = models.ForeignKey('users.User', on_delete = models.DO_NOTHING, verbose_name='发布者')
    is_choiced = models.BooleanField(default = False, verbose_name = '已有学生选择')
    tags = models.ManyToManyField(Tag, verbose_name='选题标签', blank=True)
    need_verify = models.BooleanField(default = True, verbose_name='待审核')
    collection = GenericRelation('student.Collection')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = '论文题目'
        ordering = ['-pub_date']
        unique_together = (('title', 'publisher'))

    def getCollege(self):
        if self.publisher.person == 'student':
            return self.publisher.student.college
        elif self.publisher.person == 'teacher':
            return self.publisher.teacher.college
        else:
            return None
    getCollege.shor_description = '学院名称'
    