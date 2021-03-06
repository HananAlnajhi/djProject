# Generated by Django 4.0.1 on 2022-02-08 08:09

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('orgin', models.CharField(max_length=100)),
                ('imges', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Users',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('kind', models.CharField(max_length=100)),
                ('descreption', models.TextField()),
                ('expir_date', models.DateField()),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('imges', models.ImageField(upload_to='photos/%y/%m/%d')),
                ('DT', models.DateTimeField(default=datetime.datetime.now)),
                ('active', models.BooleanField(default=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='makeup.brand')),
            ],
        ),
    ]
