# Generated by Django 3.0.7 on 2020-08-08 19:11

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reprohack', '0003_auto_20200808_1722'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='review',
            name='lead_reviewer',
        ),
        migrations.RemoveField(
            model_name='review',
            name='other_reviewers',
        ),
        migrations.CreateModel(
            name='PaperReviewer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lead_review', models.BooleanField(default=True)),
                ('review', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='reprohack.Review')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='review',
            name='reviewers',
            field=models.ManyToManyField(through='reprohack.PaperReviewer', to=settings.AUTH_USER_MODEL),
        ),
    ]
