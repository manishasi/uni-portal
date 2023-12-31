# Generated by Django 4.2.3 on 2023-07-13 12:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0003_customuser_groups_customuser_user_permissions_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agent',
            name='student',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.student'),
        ),
        migrations.AlterField(
            model_name='staff',
            name='agent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='student.agent'),
        ),
    ]
