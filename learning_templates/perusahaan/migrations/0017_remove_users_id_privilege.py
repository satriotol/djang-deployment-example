# Generated by Django 3.0.3 on 2020-06-26 12:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0016_auto_20200626_1930'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='users',
            name='id_privilege',
        ),
    ]
