# Generated by Django 2.2.15 on 2022-12-21 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0005_auto_20221221_1740'),
    ]

    operations = [
        migrations.AddField(
            model_name='city',
            name='province_id',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]