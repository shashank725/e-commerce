# Generated by Django 3.2.8 on 2021-10-21 05:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_auto_20211016_1246'),
    ]

    operations = [
        migrations.RenameField(
            model_name='orderitem',
            old_name='qunatity',
            new_name='quantity',
        ),
    ]
