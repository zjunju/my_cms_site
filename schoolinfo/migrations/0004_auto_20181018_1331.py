# Generated by Django 2.1.2 on 2018-10-18 05:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('schoolinfo', '0003_remove_studentinfo_is_register'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentinfo',
            options={'managed': False},
        ),
    ]
