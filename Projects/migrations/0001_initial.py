# Generated by Django 2.2.14 on 2021-07-08 21:09

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('project_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('project_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('duration', models.DurationField()),
                ('status', models.CharField(default='to-do', max_length=20, verbose_name='status')),
                ('image', models.ImageField(default='default.jpg', upload_to='pictures')),
            ],
        ),
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('task_id', models.AutoField(primary_key=True, serialize=False, unique=True)),
                ('task_name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('start_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('end_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('project_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Projects.Projects')),
            ],
        ),
    ]
