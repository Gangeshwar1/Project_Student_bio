# Generated by Django 4.1.1 on 2022-10-07 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu_info', '0004_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=12),
        ),
    ]