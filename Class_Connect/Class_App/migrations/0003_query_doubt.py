# Generated by Django 5.0.6 on 2024-08-11 10:24

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Class_App', '0002_feedback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query_Doubt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=100)),
                ('member_id', models.CharField(default='null', max_length=46)),
                ('email', models.CharField(max_length=100)),
                ('Question', models.TextField()),
                ('Answer', models.TextField(default='')),
                ('Question_date', models.DateField(default=django.utils.timezone.now)),
                ('Answer_date', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
