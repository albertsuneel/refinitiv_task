# Generated by Django 2.2.24 on 2021-07-11 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210708_1738'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='timestamp',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
