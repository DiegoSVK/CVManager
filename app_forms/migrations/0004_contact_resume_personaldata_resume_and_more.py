# Generated by Django 5.1.1 on 2024-10-26 00:57

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0003_academicformation_resume'),
        ('cv_platform', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cv_platform.resume'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personaldata',
            name='resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cv_platform.resume'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='workexperience',
            name='resume',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='cv_platform.resume'),
            preserve_default=False,
        ),
    ]
