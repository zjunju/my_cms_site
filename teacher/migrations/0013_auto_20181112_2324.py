# Generated by Django 2.1.2 on 2018-11-12 23:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('teacher', '0012_teacher_rest_number'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='teacher',
            options={'ordering': ['-rest_number'], 'verbose_name_plural': '教师'},
        ),
    ]
