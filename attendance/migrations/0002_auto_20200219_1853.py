# Generated by Django 3.0.2 on 2020-02-19 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('attendance', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='attendance',
            old_name='Course',
            new_name='course',
        ),
    ]