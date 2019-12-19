# Generated by Django 2.2.4 on 2019-10-13 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0009_sale_orderid'),
    ]

    operations = [
        migrations.AddField(
            model_name='sale',
            name='status',
            field=models.TextField(choices=[('I', 'Initialized'), ('P', 'Payed for'), ('O', 'Ordered'), ('R', 'Recieved by Isaac'), ('D', 'Delivered')], db_index=True, default='I'),
        ),
    ]