# Generated by Django 3.0.3 on 2020-08-22 16:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0005_auto_20200821_1717'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='productmodel',
            name='pid',
        ),
        migrations.AddField(
            model_name='productmodel',
            name='id',
            field=models.AutoField(auto_created=True, default=0, primary_key=True, serialize=False, verbose_name='ID'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='productmodel',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=9),
        ),
        migrations.CreateModel(
            name='ProductMessage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('customermsg', models.TextField()),
                ('customerreply', models.TextField()),
                ('custid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.UserModel')),
                ('productid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.ProductModel')),
            ],
        ),
    ]
