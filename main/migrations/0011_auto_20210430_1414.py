# Generated by Django 3.1.7 on 2021-04-30 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_auto_20210429_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='citizen',
            name='city',
            field=models.CharField(choices=[('Mumbai', 'Mumbai'), ('Nagpur', 'Nagpur'), ('Pune', 'Pune')], max_length=256),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='mobno',
            field=models.CharField(max_length=256),
        ),
        migrations.AlterField(
            model_name='citizen',
            name='timeslot',
            field=models.CharField(choices=[('10am to 1am', '10am to 1am'), ('2pm to 6pm', '2pm to 6pm')], max_length=256),
        ),
        migrations.AlterField(
            model_name='vac_center',
            name='city',
            field=models.CharField(choices=[('Mumbai', 'Mumbai'), ('Nagpur', 'Nagpur'), ('Pune', 'Pune')], max_length=256),
        ),
    ]