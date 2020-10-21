# Generated by Django 3.1.2 on 2020-10-20 20:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20201016_1734'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='utilizacao',
            name='alters_data',
        ),
        migrations.RemoveField(
            model_name='utilizacao',
            name='valor',
        ),
        migrations.AddField(
            model_name='utilizacao',
            name='usuario',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app.cadastro'),
        ),
    ]
