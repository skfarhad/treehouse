# Generated by Django 2.1.1 on 2019-09-13 04:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_auto_20180928_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(6, 'Address'), (0, 'Blog post'), (8, 'Type4'), (4, 'About'), (7, 'Type3'), (1, 'Quote'), (5, 'Resume'), (9, 'Type5'), (2, 'Service'), (3, 'Project'), (10, 'Type6')], default=0),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(3, 'Quote'), (8, 'Type4'), (5, 'Type1'), (4, 'Address'), (0, 'Name'), (1, 'Tagline'), (7, 'Type3'), (9, 'Type5'), (2, 'Email'), (6, 'Type2'), (10, 'Type6')], default=0),
        ),
    ]
