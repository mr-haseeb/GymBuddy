# Generated by Django 2.0.7 on 2018-08-02 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_remove_profile_age'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='activity1',
            field=models.CharField(blank=True, max_length=50),
        ),
    ]
