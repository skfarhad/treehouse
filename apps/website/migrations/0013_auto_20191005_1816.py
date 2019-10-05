# Generated by Django 2.2 on 2019-10-05 18:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0012_auto_20191005_1751'),
    ]

    operations = [
        migrations.RenameField(
            model_name='paragraph',
            old_name='image',
            new_name='image_path',
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(4, 'About'), (0, 'Normal'), (1, 'Quote'), (2, 'Service'), (9, 'Type5'), (7, 'Type3'), (5, 'Short-Bio'), (10, 'Type6'), (8, 'Type4'), (3, 'Project'), (6, 'Address')], default=0),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Tagline'), (8, 'Type4'), (0, 'Name'), (3, 'Quote'), (5, 'Type1'), (7, 'Type3'), (9, 'Type5'), (6, 'Type2'), (10, 'Type6'), (2, 'Email'), (4, 'Address')], default=0),
        ),
    ]
