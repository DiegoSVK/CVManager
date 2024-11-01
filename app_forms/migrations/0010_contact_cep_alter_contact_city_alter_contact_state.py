# Generated by Django 5.1.1 on 2024-10-30 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_forms', '0009_contact_city_contact_state'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='cep',
            field=models.CharField(default=1, max_length=10),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='city',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='contact',
            name='state',
            field=models.CharField(max_length=50),
        ),
    ]
