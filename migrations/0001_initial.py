# Generated by Django 2.2.12 on 2021-12-22 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', max_length=20, unique=True, verbose_name='用户名')),
                ('age', models.IntegerField(default=1, verbose_name='年龄')),
            ],
        ),
    ]
