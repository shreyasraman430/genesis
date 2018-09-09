# Generated by Django 2.0.5 on 2018-08-12 00:21

import datetime
from django.db import migrations, models
import django.utils.timezone
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('originals', '0007_auto_20180812_0528'),
    ]

    operations = [
        migrations.CreateModel(
            name='ScienceQuizzine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('publish_date', models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 12, 0, 21, 36, 234336, tzinfo=utc), null=True)),
                ('title', models.CharField(max_length=200)),
                ('description', models.CharField(max_length=280)),
                ('image_file', models.ImageField(upload_to='sciencequizzine')),
            ],
        ),
        migrations.DeleteModel(
            name='ScienceQuizine',
        ),
        migrations.AlterField(
            model_name='archiveimage',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=django.utils.timezone.now, null=True),
        ),
        migrations.AlterField(
            model_name='article',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 12, 0, 21, 36, 236331, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='image',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 12, 0, 21, 36, 235334, tzinfo=utc), null=True),
        ),
        migrations.AlterField(
            model_name='video',
            name='publish_date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2018, 8, 12, 0, 21, 36, 237327, tzinfo=utc), null=True),
        ),
    ]