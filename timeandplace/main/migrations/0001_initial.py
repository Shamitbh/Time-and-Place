# Generated by Django 3.1 on 2022-11-06 21:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('DBA', models.CharField(max_length=100)),
                ('BORO', models.CharField(max_length=100)),
                ('BUILDING', models.CharField(max_length=20)),
                ('STERRT', models.CharField(max_length=40)),
                ('ZIPCODE', models.FloatField()),
                ('PHONE', models.CharField(max_length=12)),
                ('CUISION', models.CharField(max_length=20)),
                ('LATITUDE', models.FloatField()),
                ('LONGTITUDE', models.FloatField()),
            ],
        ),
    ]
