# Generated by Django 3.1.4 on 2021-08-02 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getauctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctioninfo',
            name='cantidad_reclamada',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
