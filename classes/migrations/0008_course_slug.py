# Generated by Django 2.2.6 on 2020-03-02 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_assignment_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='slug',
            field=models.CharField(blank=True, editable=False, help_text='Unique URL path to access this page. Generated by the system.', max_length=30),
        ),
    ]
