# Generated by Django 3.2.5 on 2021-07-19 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_mostfrequentquestions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mostfrequentquestions',
            name='answer',
            field=models.CharField(max_length=500),
        ),
    ]
