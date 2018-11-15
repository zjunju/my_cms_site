# Generated by Django 2.1.2 on 2018-11-13 14:00

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('announcement', '0003_auto_20181111_2157'),
    ]

    operations = [
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='计划标题')),
                ('content', models.TextField(verbose_name='计划详细内容')),
                ('start_time', models.DateField(verbose_name='开始时间')),
                ('stop_time', models.DateField(verbose_name='截至时间')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='发布者')),
            ],
            options={
                'verbose_name_plural': '计划',
            },
        ),
    ]
