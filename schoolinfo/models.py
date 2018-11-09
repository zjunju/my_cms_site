# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class StudentInfo(models.Model):
    number = models.CharField(primary_key=True, max_length=20,verbose_name = '学生学号')
    name = models.CharField(max_length=10, verbose_name = '姓名')
    class_name = models.CharField(max_length=20, verbose_name = '班级')
    college = models.CharField(max_length=30, verbose_name = '学院')
    score = models.IntegerField(blank=True, null=True, verbose_name = '毕设分数')

    class Meta:
        managed = False
        db_table = 'student_info'


class TeacherInfo(models.Model):
    number = models.CharField(primary_key=True, max_length=20, verbose_name = '教师编号')
    name = models.CharField(max_length=20, verbose_name = '姓名')
    college = models.CharField(max_length=30, verbose_name = '学院')
    job_title = models.CharField(max_length=10, verbose_name = '职称')

    class Meta:
        managed = False
        db_table = 'teacher_info'
