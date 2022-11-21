# Generated by Django 4.1.3 on 2022-11-09 12:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_rename_owner_land_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='constructionbuilding',
            name='number_of_construction',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='tree',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='crop',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(10, '10'), (9, '9'), (8, '8'), (7, '7'), (6, '6'), (5, '5'), (4, '4'), (3, '3'), (2, '2'), (1, '1')], default=1),
        ),
    ]
