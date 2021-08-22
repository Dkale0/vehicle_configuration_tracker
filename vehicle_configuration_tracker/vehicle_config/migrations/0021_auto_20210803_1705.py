# Generated by Django 3.1.7 on 2021-08-03 22:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vehicle_config', '0020_auto_20210708_1838'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='assembly',
            name='parts',
        ),
        migrations.RemoveField(
            model_name='setup',
            name='car',
        ),
        migrations.RemoveField(
            model_name='setup',
            name='setup_params',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='assemblies',
        ),
        migrations.RemoveField(
            model_name='vehicle',
            name='setups',
        ),
        migrations.AddField(
            model_name='assembly',
            name='parent_vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle_config.vehicle'),
        ),
        migrations.AddField(
            model_name='part',
            name='parent_assembly',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle_config.assembly'),
        ),
        migrations.AddField(
            model_name='setup',
            name='parent_vehicle',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle_config.vehicle'),
        ),
        migrations.AddField(
            model_name='setupparam',
            name='parent_setup',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='vehicle_config.setup'),
        ),
        migrations.AlterField(
            model_name='assembly',
            name='assemblies',
            field=models.ManyToManyField(to='vehicle_config.Assembly'),
        ),
    ]