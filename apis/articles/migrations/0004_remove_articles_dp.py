# Generated by Django 3.1.7 on 2021-04-04 05:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0003_auto_20210402_1400'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles',
            name='dp',
        ),
    ]
