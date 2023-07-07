# Generated by Django 4.2.3 on 2023-07-06 16:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0002_alter_university_scholarship_available'),
    ]

    operations = [
        migrations.AlterField(
            model_name='university',
            name='det_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='pte_score',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='toefl_no_band_less_than',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='university',
            name='toefl_score',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
