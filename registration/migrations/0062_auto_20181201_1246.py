# Generated by Django 2.1.3 on 2018-12-01 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0061_ibmhackathonregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='ibmhackathonregistration',
            name='question2',
            field=models.TextField(default=False),
        ),
        migrations.AddField(
            model_name='ibmhackathonregistration',
            name='question3',
            field=models.TextField(default=False),
        ),
        migrations.AddField(
            model_name='ibmhackathonregistration',
            name='question4',
            field=models.TextField(blank=True),
        ),
    ]