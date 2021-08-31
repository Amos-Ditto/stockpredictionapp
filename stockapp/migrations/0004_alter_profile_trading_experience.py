# Generated by Django 3.2.5 on 2021-08-15 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('stockapp', '0003_alter_profile_occupation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='trading_experience',
            field=models.CharField(choices=[('<1', 'less_than_1yr'), ('1', '1'), ('2', '2'), ('3', '3'), ('>3', 'more_than_3yrs')], max_length=10),
        ),
    ]
