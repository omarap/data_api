# Generated by Django 4.1.3 on 2023-01-13 09:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='projectaffectedperson',
            old_name='id_no',
            new_name='nin',
        ),
    ]
