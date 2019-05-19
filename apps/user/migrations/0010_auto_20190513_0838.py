# Generated by Django 2.1.7 on 2019-05-13 08:38

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0009_auto_20190513_0836'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemsg',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('e97746d5-2f3f-4ba3-88e9-87604d87da6e'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('2f985407-7b44-41fc-9de6-4cd7be8970ae'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
    ]
