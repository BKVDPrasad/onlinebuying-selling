# Generated by Django 3.0.3 on 2020-08-21 06:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_auto_20200820_2110'),
    ]

    operations = [
        migrations.AddField(
            model_name='productmodel',
            name='userid',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='app1.UserModel'),
        ),
    ]
