# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-26 20:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login_reg_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Appt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('tasks', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('all_users', models.ManyToManyField(related_name='all_appts', to='login_reg_app.User')),
                ('user_appt', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='appts_of_user', to='login_reg_app.User')),
            ],
        ),
    ]
