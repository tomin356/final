# Generated by Django 4.2.7 on 2024-02-29 07:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0005_remove_card_cover_card_pic'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='price',
            field=models.TextField(),
        ),
    ]
