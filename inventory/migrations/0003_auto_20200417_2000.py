# Generated by Django 3.0.5 on 2020-04-17 20:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0002_auto_20200417_1930'),
    ]

    operations = [
        migrations.RenameField(
            model_name='part',
            old_name='company_id',
            new_name='company',
        ),
    ]
