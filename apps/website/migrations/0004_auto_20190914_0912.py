# Generated by Django 2.2 on 2019-09-14 09:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_auto_20190913_0440'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(7, 'Type3'), (3, 'Project'), (0, 'Blog post'), (4, 'About'), (1, 'Quote'), (9, 'Type5'), (6, 'Address'), (2, 'Service'), (10, 'Type6'), (8, 'Type4'), (5, 'Resume')], default=0),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(5, 'Type1'), (7, 'Type3'), (4, 'Address'), (0, 'Name'), (6, 'Type2'), (3, 'Quote'), (9, 'Type5'), (2, 'Email'), (10, 'Type6'), (8, 'Type4'), (1, 'Tagline')], default=0),
        ),
    ]
