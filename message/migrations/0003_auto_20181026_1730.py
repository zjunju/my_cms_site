# Generated by Django 2.1.2 on 2018-10-26 09:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_auto_20181024_0946'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'ordering': ['-send_time'], 'verbose_name_plural': '消息'},
        ),
    ]
