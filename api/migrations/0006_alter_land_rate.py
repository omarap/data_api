# Generated by Django 4.1.3 on 2022-11-07 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_alter_land_options_remove_land_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='land',
            name='rate',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]
