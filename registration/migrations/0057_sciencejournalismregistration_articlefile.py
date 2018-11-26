# Generated by Django 2.1.3 on 2018-11-26 17:05

from django.db import migrations, models
import registration.field_helpers
import registration.models


class Migration(migrations.Migration):

    dependencies = [
        ('registration', '0056_sciencejournalismregistration'),
    ]

    operations = [
        migrations.AddField(
            model_name='sciencejournalismregistration',
            name='articleFile',
            field=models.FileField(blank=True, max_length=600, upload_to=registration.models.ScienceJournalismRegistration.filePathGenerate, validators=[registration.field_helpers.lasya_file_validation]),
        ),
    ]