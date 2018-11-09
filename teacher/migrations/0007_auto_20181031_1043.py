# Generated by Django 2.1.2 on 2018-10-31 10:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0006_remove_teacher_rest_number'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teacher',
            name='email',
            field=models.CharField(blank=True, max_length=30, null=True, verbose_name='邮箱'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='introduction',
            field=models.TextField(blank=True, null=True, verbose_name='个人简介'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='max_number',
            field=models.PositiveIntegerField(default=0, verbose_name='最大指导学生人数'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=11, null=True, verbose_name='手机号码'),
        ),
        migrations.AlterField(
            model_name='teacher',
            name='user',
            field=models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL, verbose_name='用户名'),
        ),
    ]