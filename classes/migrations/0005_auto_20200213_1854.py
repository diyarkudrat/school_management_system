# Generated by Django 3.0.2 on 2020-02-13 18:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_auto_20200211_2104'),
    ]

    operations = [
        migrations.AddField(
            model_name='assignment',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='classes.Course'),
        ),
        migrations.AlterField(
            model_name='course',
            name='assigments',
            field=models.ManyToManyField(blank=True, null=True, related_name='course_assignments', to='classes.Assignment'),
        ),
    ]
