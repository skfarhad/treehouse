# Generated by Django 2.2 on 2019-10-05 17:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_auto_20191005_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='image_path',
            field=models.ImageField(blank=True, null=True, upload_to='para_images/'),
        ),
        migrations.AlterField(
            model_name='workhistory',
            name='image_path',
            field=models.ImageField(blank=True, null=True, upload_to='para_images/'),
        ),
    ]