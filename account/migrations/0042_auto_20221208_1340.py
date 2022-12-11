# Generated by Django 2.2 on 2022-12-08 13:40

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0041_profile_feedback_submitted'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='date_of_birth',
            field=models.DateField(blank=True, default=datetime.date(2022, 12, 8), null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='gender_identity',
            field=models.CharField(choices=[('Woman', 'Woman'), ('Man', 'Man'), ('Transgender', 'Transgender'), ('Non-binary', 'Non-binary')], default='N/A', max_length=15),
        ),
    ]