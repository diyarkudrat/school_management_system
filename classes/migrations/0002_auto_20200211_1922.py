# Generated by Django 2.2.6 on 2020-02-11 19:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TakenCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course_average', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('exam', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('total', models.PositiveIntegerField(blank=True, default=0, null=True)),
                ('grade', models.CharField(blank=True, choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('F', 'F')], max_length=1)),
                ('comment', models.CharField(blank=True, choices=[('PASS', 'PASS'), ('FAIL', 'FAIL')], max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='course',
            name='course_average',
        ),
        migrations.RemoveField(
            model_name='course',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='course',
            name='grade',
        ),
        migrations.RemoveField(
            model_name='course',
            name='total',
        ),
        migrations.RemoveField(
            model_name='semester',
            name='session',
        ),
        migrations.DeleteModel(
            name='Session',
        ),
        migrations.AddField(
            model_name='takencourse',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='taken_courses', to='classes.Course'),
        ),
        migrations.AddField(
            model_name='takencourse',
            name='student',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.Student'),
        ),
    ]
