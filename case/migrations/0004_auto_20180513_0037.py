# Generated by Django 2.0.3 on 2018-05-12 14:37

from django.db import migrations
import django.db.models.manager


class Migration(migrations.Migration):

    dependencies = [
        ('case', '0003_auto_20180512_1949'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='case',
            managers=[
                ('manager', django.db.models.manager.Manager()),
            ],
        ),
    ]
