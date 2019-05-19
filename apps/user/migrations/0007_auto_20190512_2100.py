# Generated by Django 2.1.7 on 2019-05-12 21:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0006_auto_20190512_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemsg',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('b71a1994-50e5-4e68-9fa9-06358834e1d8'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('3e0461de-9609-4447-828c-7faf30b7f17d'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
    ]
