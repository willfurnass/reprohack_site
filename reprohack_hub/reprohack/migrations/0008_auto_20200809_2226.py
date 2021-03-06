# Generated by Django 3.0.7 on 2020-08-09 22:26

import datetime
import django.contrib.gis.db.models.fields
from django.db import migrations, models
import markdownx.models


class Migration(migrations.Migration):

    dependencies = [
        ('reprohack', '0007_auto_20200809_1917'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='event',
            name='venue',
        ),
        migrations.AddField(
            model_name='event',
            name='address1',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='address2',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='city',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='country',
            field=models.CharField(default='', max_length=60),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='geom',
            field=django.contrib.gis.db.models.fields.PointField(blank=True, null=True, srid=4326),
        ),
        migrations.AddField(
            model_name='event',
            name='postcode',
            field=models.CharField(default='', max_length=15),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='event',
            name='venue_description',
            field=markdownx.models.MarkdownxField(default='', verbose_name='Venue description (eg. entrance, parking etc.)'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='event',
            name='end_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 14, 0)),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_time',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 10, 10, 0)),
        ),
        migrations.AlterField(
            model_name='paper',
            name='doi',
            field=models.CharField(max_length=200, verbose_name='DOI (eg. 10.1000/xyz123)'),
        ),
        migrations.AlterField(
            model_name='review',
            name='operating_system_detail',
            field=models.CharField(max_length=100, verbose_name='What operating system were you using (eg. Ubuntu 14.04.6 LTS, macOS 10.15 or Windows 10 Pro)?'),
        ),
        migrations.DeleteModel(
            name='Author',
        ),
        migrations.DeleteModel(
            name='Venue',
        ),
    ]
