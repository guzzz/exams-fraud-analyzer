# Generated by Django 4.2.11 on 2024-03-09 01:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('persons', '0001_initial'),
        ('monitors', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Title')),
                ('base_blood_pressure', models.PositiveIntegerField(verbose_name='Base Blood Pressure')),
                ('base_heart_rate', models.PositiveIntegerField(verbose_name='Base Heart Rate')),
                ('start_date', models.DateTimeField(verbose_name='Start Date')),
                ('end_date', models.DateTimeField(verbose_name='End Date')),
                ('is_fraud', models.BooleanField(null=True, verbose_name='Is Fraud ?')),
                ('blood_pressure_monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blood_pressure_monitor', to='monitors.monitor')),
                ('heart_rate_monitor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='heart_rate_monitor', to='monitors.monitor')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='persons.person')),
            ],
        ),
    ]