# Generated by Django 2.1.2 on 2018-11-06 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0007_thesis_need_verify'),
    ]

    operations = [
        migrations.AlterField(
            model_name='thesis',
            name='tags',
            field=models.ManyToManyField(blank=True, null=True, to='thesis.Tag', verbose_name='选题标签'),
        ),
    ]