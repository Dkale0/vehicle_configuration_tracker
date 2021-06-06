# Generated by Django 3.1.7 on 2021-06-05 03:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_config', '0009_auto_20210604_2231'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vehicle',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='vehicle',
            name='setups',
            field=models.ManyToManyField(blank=True, null=True, to='vehicle_config.Setup'),
        ),
    ]
