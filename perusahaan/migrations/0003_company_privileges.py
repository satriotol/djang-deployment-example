# Generated by Django 3.0.3 on 2020-06-23 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0002_auto_20200623_2221'),
    ]

    operations = [
        migrations.CreateModel(
            name='company_privileges',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
            ],
        ),
    ]
