# Generated by Django 3.1.7 on 2021-04-28 15:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='citizen',
            name='age',
            field=models.IntegerField(default=46),
            preserve_default=False,
        ),
    ]
