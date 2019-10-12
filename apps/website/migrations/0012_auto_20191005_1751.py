# Generated by Django 2.2 on 2019-10-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0011_auto_20191005_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paragraph',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='para_images/'),
        ),
        migrations.AlterField(
            model_name='paragraph',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(9, 'Type5'), (3, 'Project'), (6, 'Address'), (4, 'About'), (8, 'Type4'), (5, 'Short-Bio'), (7, 'Type3'), (1, 'Quote'), (0, 'Normal'), (2, 'Service'), (10, 'Type6')], default=0),
        ),
        migrations.AlterField(
            model_name='textfield',
            name='type',
            field=models.PositiveSmallIntegerField(choices=[(4, 'Address'), (9, 'Type5'), (3, 'Quote'), (7, 'Type3'), (0, 'Name'), (8, 'Type4'), (1, 'Tagline'), (6, 'Type2'), (5, 'Type1'), (2, 'Email'), (10, 'Type6')], default=0),
        ),
    ]