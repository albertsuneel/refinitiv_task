# Generated by Django 2.2.24 on 2021-07-08 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20210706_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='transaction_id',
            field=models.CharField(max_length=16),
        ),
    ]
