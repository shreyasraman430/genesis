# Generated by Django 2.0.5 on 2018-09-15 21:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0010_auto_20180913_0537'),
    ]

    operations = [
        migrations.AddField(
            model_name='footprintsregistration',
            name='last_modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='footprintsregistration',
            name='submit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lasyaregistration',
            name='last_modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='lasyaregistration',
            name='submit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prosceniumregistration',
            name='last_modify_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='prosceniumregistration',
            name='submit_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
