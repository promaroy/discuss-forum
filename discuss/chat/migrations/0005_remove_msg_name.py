# Generated by Django 2.2.1 on 2019-06-02 13:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_auto_20190602_1222'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msg',
            name='name',
        ),
    ]
