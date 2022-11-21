# Generated by Django 4.1.3 on 2022-11-09 13:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0011_alter_crop_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='rating',
            field=models.PositiveSmallIntegerField(choices=[(4, '4'), (5, '5'), (6, '6'), (7, '7'), (8, '8'), (9, '9'), (10, '10')], default=5),
        ),
    ]
