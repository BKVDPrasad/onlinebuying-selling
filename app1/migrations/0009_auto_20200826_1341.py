# Generated by Django 3.0.3 on 2020-08-26 08:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0008_auto_20200826_1339'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmodel',
            old_name='productid',
            new_name='pid',
        ),
    ]
