# Generated by Django 2.2.6 on 2020-03-02 18:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0003_auto_20200225_1939'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='courseattendance',
            name='students',
        ),
    ]
