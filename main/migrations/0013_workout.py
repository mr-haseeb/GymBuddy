# Generated by Django 2.1 on 2018-08-26 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20180807_1022'),
    ]

    operations = [
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('what', models.CharField(blank=True, max_length=100)),
                ('gym', models.CharField(blank=True, max_length=100)),
                ('time', models.CharField(blank=True, max_length=100)),
            ],
        ),
    ]
