# Generated by Django 4.2.3 on 2023-07-06 16:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_alter_university_det_score_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='scholarship_available',
            field=models.BooleanField(default=False),
        ),
    ]
