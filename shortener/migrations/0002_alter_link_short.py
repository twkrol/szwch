# Generated by Django 4.0.6 on 2022-07-22 14:42

from django.db import migrations, models
import shortener.models


class Migration(migrations.Migration):

    dependencies = [
        ('shortener', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='link',
            name='short',
            field=models.CharField(default=shortener.models._make_short_code, max_length=8),
        ),
    ]
