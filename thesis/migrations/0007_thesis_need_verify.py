# Generated by Django 2.1.2 on 2018-11-05 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('thesis', '0006_auto_20181031_1043'),
    ]

    operations = [
        migrations.AddField(
            model_name='thesis',
            name='need_verify',
            field=models.BooleanField(default=False, verbose_name='是否需要审核'),
        ),
    ]
