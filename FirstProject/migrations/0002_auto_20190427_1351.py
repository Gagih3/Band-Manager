# Generated by Django 2.2 on 2019-04-27 09:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('FirstProject', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_image',
            field=models.ImageField(blank=True, upload_to='profile_image'),
        ),
    ]