# Generated by Django 4.0.1 on 2022-02-08 19:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('makeup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='imges',
            field=models.ImageField(upload_to='media/photos/%y/%m/%d'),
        ),
    ]