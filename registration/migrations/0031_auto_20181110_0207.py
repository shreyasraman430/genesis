# Generated by Django 2.1.1 on 2018-11-09 20:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0030_pisregistration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pisregistration',
            name='ideaAbstract',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pisregistration',
            name='marketResearch',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pisregistration',
            name='motivation',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pisregistration',
            name='prospects',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='pisregistration',
            name='prototyping',
            field=models.TextField(blank=True),
        ),
    ]
