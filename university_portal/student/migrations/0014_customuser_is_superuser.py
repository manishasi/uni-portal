# Generated by Django 4.2.3 on 2023-07-07 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0013_alter_student_contact_number_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='is_superuser',
            field=models.BooleanField(default=False),
        ),
    ]
