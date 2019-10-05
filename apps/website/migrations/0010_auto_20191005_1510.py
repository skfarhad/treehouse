# Generated by Django 2.2 on 2019-10-05 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0009_auto_20191005_1508'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(10, 'Type6'), (6, 'Address'), (1, 'Quote'), (5, 'Short-Bio'), (0, 'Normal'), (2, 'Service'), (3, 'Project'), (9, 'Type5'), (8, 'Type4'), (4, 'About'), (7, 'Type3')], default=0),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(2, 'Email'), (8, 'Type4'), (3, 'Quote'), (1, 'Tagline'), (9, 'Type5'), (10, 'Type6'), (4, 'Address'), (6, 'Type2'), (7, 'Type3'), (5, 'Type1'), (0, 'Name')], default=0),
        ),
    ]
