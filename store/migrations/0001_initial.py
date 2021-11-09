# Generated by Django 3.2.9 on 2021-11-08 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=200)),
                ('product_category', models.CharField(max_length=200)),
                ('description', models.TextField(max_length=500)),
                ('price', models.IntegerField()),
                ('images', models.ImageField(upload_to='photos/products')),
            ],
        ),
    ]
