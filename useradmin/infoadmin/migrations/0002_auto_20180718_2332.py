# Generated by Django 2.0.6 on 2018-07-18 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('infoadmin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='crt_date',
            field=models.DateTimeField(),
        ),
    ]
