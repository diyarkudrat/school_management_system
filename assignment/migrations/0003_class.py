# Generated by Django 2.2.6 on 2020-01-30 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('assignment', '0002_auto_20200130_2137'),
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('students', models.ManyToManyField(to='assignment.Student')),
            ],
        ),
    ]
