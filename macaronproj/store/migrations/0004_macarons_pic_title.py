# Generated by Django 2.1.7 on 2019-05-21 17:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_auto_20190520_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='macarons',
            name='pic_title',
            field=models.TextField(default=''),
        ),
    ]
