# Generated by Django 2.0.3 on 2018-05-12 09:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0002_auto_20180512_1946'),
    ]

    operations = [
        migrations.RenameField(
            model_name='casestatus',
            old_name='cases_status',
            new_name='case_status',
        ),
    ]