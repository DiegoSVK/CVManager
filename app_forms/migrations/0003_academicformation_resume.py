# Generated by Django 5.1.1 on 2024-10-26 00:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0002_remove_contact_personal_data_and_more'),
        ('cv_platform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='academicformation',
            name='resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cv_platform.resume'),
            preserve_default=False,
        ),
    ]