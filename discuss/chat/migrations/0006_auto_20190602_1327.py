# Generated by Django 2.2.1 on 2019-06-02 13:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0005_remove_msg_name'),
    ]

    operations = [
        migrations.RenameField(
            model_name='msg',
            old_name='content',
            new_name='name',
        ),
    ]
