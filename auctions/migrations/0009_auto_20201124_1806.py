# Generated by Django 3.1.2 on 2020-11-24 17:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_auto_20201122_0054'),
    ]

    operations = [
        migrations.AddField(
            model_name='bid',
            name='listing',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='bid_listingid', to='auctions.listing'),
        ),
        migrations.AlterField(
            model_name='bid',
            name='bid_listingid',
            field=models.CharField(default=True, max_length=64),
            preserve_default=False,
        ),
    ]