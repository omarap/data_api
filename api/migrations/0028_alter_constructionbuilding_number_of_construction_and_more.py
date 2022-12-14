# Generated by Django 4.1.3 on 2022-12-12 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0027_alter_constructionbuilding_pap_alter_crop_pap_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='constructionbuilding',
            name='number_of_construction',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='constructionbuilding',
            name='rate',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='constructionbuilding',
            name='size',
            field=models.FloatField(default=0),
        ),
        migrations.AlterField(
            model_name='tree',
            name='quantity',
            field=models.PositiveSmallIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='tree',
            name='rate',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
