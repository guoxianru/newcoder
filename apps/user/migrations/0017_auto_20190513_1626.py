# Generated by Django 2.1.7 on 2019-05-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0016_auto_20190513_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leavemsg',
            name='unique_id',
            field=models.CharField(default='reward_uuid=jd5vKaYL', max_length=36, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='user',
            name='unique_id',
            field=models.CharField(default='reward_uuid=MWC7meFe', max_length=36, unique=True, verbose_name='唯一标识符'),
        ),
    ]
