# Generated by Django 2.2.1 on 2019-06-02 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0003_remove_msg_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='msg',
            name='name',
            field=models.CharField(default='abc', max_length=25),
        ),
        migrations.AlterField(
            model_name='msg',
            name='content',
            field=models.TextField(),
        ),
    ]
