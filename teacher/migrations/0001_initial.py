# Generated by Django 2.1.2 on 2018-10-15 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('schoolinfo', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('teacherinfo_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='schoolinfo.TeacherInfo')),
                ('introduction', models.TextField(blank=True, null=True)),
                ('phonenumber', models.CharField(blank=True, default='', max_length=11, null=True)),
                ('email', models.CharField(blank=True, default='', max_length=30, null=True)),
                ('max_number', models.PositiveIntegerField(default=0)),
            ],
            bases=('schoolinfo.teacherinfo',),
        ),
    ]
