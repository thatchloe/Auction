# Generated by Django 3.1.2 on 2020-11-28 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_auto_20201128_2147'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(null=True),
        ),
    ]
