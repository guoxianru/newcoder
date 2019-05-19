# Generated by Django 2.1.7 on 2019-05-12 20:39

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_auto_20190512_2037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemsg',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('712b7cb5-fb2e-4676-8396-614a60bdadac'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('811efcbf-33a4-49f5-b156-20331c5181ca'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
    ]
