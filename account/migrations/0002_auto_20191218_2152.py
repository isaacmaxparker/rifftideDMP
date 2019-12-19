# Generated by Django 2.2.4 on 2019-12-18 21:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='birthdate',
        ),
        migrations.AddField(
            model_name='user',
            name='loginname',
            field=models.TextField(default='NONE'),
        ),
        migrations.AddField(
            model_name='user',
            name='name',
            field=models.TextField(default='NONE'),
        ),
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.TextField(choices=[('A', 'Active'), ('I', 'Inactive')], db_index=True, default='A'),
        ),
        migrations.AddField(
            model_name='user',
            name='voicepart',
            field=models.TextField(default='NONE'),
        ),
        migrations.AlterField(
            model_name='user',
            name='password',
            field=models.TextField(default='NONE'),
        ),
    ]
