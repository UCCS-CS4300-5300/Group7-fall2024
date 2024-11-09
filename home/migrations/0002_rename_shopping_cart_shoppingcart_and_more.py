# Generated by Django 5.1.2 on 2024-11-08 23:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Shopping_Cart',
            new_name='ShoppingCart',
        ),
        migrations.AddField(
            model_name='motherboard',
            name='supported_storage_types',
            field=models.ManyToManyField(to='home.storagetype'),
        ),
    ]