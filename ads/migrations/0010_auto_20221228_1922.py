# Generated by Django 2.2.15 on 2022-12-28 18:22

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ads', '0009_auto_20221228_1901'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ads',
            name='description',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
