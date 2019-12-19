# Generated by Django 2.2.4 on 2019-12-18 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_sale_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sale',
            name='status',
            field=models.TextField(choices=[('I', 'Initialized'), ('P', 'Payed for'), ('O', 'Ordered'), ('R', 'Recieved by Isaac'), ('D', 'Delivered'), ('E', 'Erased')], db_index=True, default='I'),
        ),
    ]
