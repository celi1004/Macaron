# Generated by Django 2.1.7 on 2019-05-20 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0002_macarons'),
    ]

    operations = [
        migrations.RenameField(
            model_name='macarons',
            old_name='image',
            new_name='picture',
        ),
    ]