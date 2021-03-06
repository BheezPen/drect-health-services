# Generated by Django 3.2.13 on 2022-06-11 15:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rpms_main', '0004_appointments_is_discharged'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='about',
            field=models.TextField(default='I am a Doctor'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='fields_of_expertise',
            field=models.CharField(default='Doctor', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='hourly_fee',
            field=models.PositiveIntegerField(default='20'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='patients_treated',
            field=models.PositiveIntegerField(default='3'),
            preserve_default=False,
        ),
    ]
