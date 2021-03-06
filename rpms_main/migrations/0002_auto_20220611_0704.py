# Generated by Django 3.2.13 on 2022-06-11 07:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('rpms_main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='appointments',
            options={'verbose_name_plural': 'Appointment'},
        ),
        migrations.AddField(
            model_name='appointments',
            name='complaint',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='doctor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor_appointment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='appointments',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_appointment', to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_patient', models.BooleanField(default=True)),
                ('appointment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient_appointment', to='rpms_main.appointments')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='patient', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_a_doctor', models.BooleanField(default=False)),
                ('appointments', models.ManyToManyField(related_name='appointments', to='rpms_main.Appointments')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctor', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
