# Generated by Django 3.1.2 on 2020-11-15 17:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auto_20201115_1806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='category',
            field=models.CharField(max_length=64),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]
