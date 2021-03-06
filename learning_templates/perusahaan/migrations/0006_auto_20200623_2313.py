# Generated by Django 3.0.3 on 2020-06-23 16:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('perusahaan', '0005_vacation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='id_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.company'),
        ),
        migrations.AlterField(
            model_name='users',
            name='id_privilege',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.company_privileges'),
        ),
        migrations.AlterField(
            model_name='vacation',
            name='id_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='perusahaan.users'),
        ),
    ]
