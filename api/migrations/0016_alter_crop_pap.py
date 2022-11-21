# Generated by Django 4.1.3 on 2022-11-17 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_crop_pap'),
    ]

    operations = [
        migrations.AlterField(
            model_name='crop',
            name='pap',
            field=models.ForeignKey(limit_choices_to={'is_staff': True}, on_delete=django.db.models.deletion.CASCADE, related_name='pap_crops', to='api.projectaffectedperson'),
        ),
    ]
