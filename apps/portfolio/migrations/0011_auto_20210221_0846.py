# Generated by Django 2.2 on 2021-02-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0010_auto_20210221_0843'),
    ]

    operations = [
        migrations.AddField(
            model_name='service',
            name='show',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='workhistory',
            name='show',
            field=models.BooleanField(default=True),
        ),
    ]
