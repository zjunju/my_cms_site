# Generated by Django 2.1.2 on 2018-11-03 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0009_auto_20181031_1043'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collection',
            options={'ordering': ['pk'], 'verbose_name_plural': '学生收藏选题表'},
        ),
        migrations.AlterField(
            model_name='student',
            name='is_choiced_thesis',
            field=models.BooleanField(default=False, verbose_name='是否选题'),
        ),
    ]