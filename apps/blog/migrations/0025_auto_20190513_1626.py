# Generated by Django 2.1.7 on 2019-05-13 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0024_auto_20190513_1611'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='title',
            field=models.CharField(max_length=128, unique=True, verbose_name='文章标题'),
        ),
        migrations.AlterField(
            model_name='article',
            name='unique_id',
            field=models.CharField(default='reward_uuid=rVyLNhgL', max_length=36, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='articlecol',
            name='unique_id',
            field=models.CharField(default='reward_uuid=rc3KXtFQ', max_length=36, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='unique_id',
            field=models.CharField(default='reward_uuid=mgDFC4bB', max_length=36, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='unique_id',
            field=models.CharField(default='reward_uuid=dgBZT6Bx', max_length=36, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='unique_id',
            field=models.CharField(default='reward_uuid=pboPTBES', max_length=36, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='type',
            name='unique_id',
            field=models.CharField(default='reward_uuid=EJ86Vu2U', max_length=36, unique=True, verbose_name='唯一标识符'),
        ),
    ]
