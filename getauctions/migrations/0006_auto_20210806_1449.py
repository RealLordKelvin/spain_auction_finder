# Generated by Django 3.1.4 on 2021-08-06 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('getauctions', '0005_auto_20210806_1222'),
    ]

    operations = [
        migrations.RenameField(
            model_name='auctioninfo',
            old_name='comunidad',
            new_name='provincia',
        ),
        migrations.AddField(
            model_name='auctioninfo',
            name='correo_electronico',
            field=models.CharField(blank=True, default='', max_length=300, null=True),
        ),
    ]
