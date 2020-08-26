# Generated by Django 3.0.3 on 2020-08-22 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0006_auto_20200822_2221'),
    ]

    operations = [
        migrations.RenameField(
            model_name='productmessage',
            old_name='custid',
            new_name='fromid',
        ),
        migrations.AddField(
            model_name='productmessage',
            name='toid',
            field=models.IntegerField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmessage',
            name='customermsg',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='productmessage',
            name='customerreply',
            field=models.TextField(null=True),
        ),
    ]