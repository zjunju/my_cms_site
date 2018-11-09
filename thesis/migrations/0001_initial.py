# Generated by Django 2.1.2 on 2018-10-15 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('object_id', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Thesis',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('content', models.TextField()),
                ('pub_date', models.DateField(auto_now_add=True)),
                ('is_choiced', models.BooleanField(default=False, verbose_name='已有学生选择')),
            ],
            options={
                'verbose_name_plural': '论文题目',
                'ordering': ['-pub_date'],
            },
        ),
    ]
