# Generated by Django 3.0.3 on 2020-08-20 15:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ptype', models.CharField(max_length=40)),
                ('pname', models.CharField(max_length=40)),
                ('price', models.DecimalField(decimal_places=2, max_digits=5)),
                ('descriptionproduct', models.TextField()),
                ('image', models.ImageField(upload_to='products/')),
            ],
        ),
    ]
