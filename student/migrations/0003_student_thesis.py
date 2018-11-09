# Generated by Django 2.1.2 on 2018-10-15 15:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('thesis', '0001_initial'),
        ('student', '0002_student_teacher'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='thesis',
            field=models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.DO_NOTHING, to='thesis.Thesis'),
        ),
    ]