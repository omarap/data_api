# Generated by Django 4.1.3 on 2023-01-21 16:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_remove_tenuretype_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='constructionlist',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='croplist',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='landlist',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='treelist',
            name='owner',
        ),
    ]