# Generated by Django 4.1.1 on 2022-10-07 07:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stu_info', '0003_alter_student_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
