# Generated by Django 2.2.1 on 2019-05-30 15:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_msg_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='msg',
            name='name',
        ),
    ]
