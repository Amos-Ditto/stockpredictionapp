# Generated by Django 3.2.5 on 2021-08-15 21:05

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0006_stockprices'),
    ]

    operations = [
        migrations.AddField(
            model_name='stockprices',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
