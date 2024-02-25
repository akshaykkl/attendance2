# Generated by Django 5.0.2 on 2024-02-24 13:21

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_remove_student_last_name_remove_teacher_last_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='principal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.IntegerField()),
            ],
        ),
        migrations.RenameField(
            model_name='student',
            old_name='first_name',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='teacher',
            old_name='first_name',
            new_name='name',
        ),
        migrations.CreateModel(
            name='hod',
            fields=[
                ('hod_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=120)),
                ('email', models.EmailField(max_length=254)),
                ('contact_number', models.IntegerField()),
                ('dept', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.department')),
            ],
        ),
    ]