# Generated by Django 2.1.7 on 2019-05-13 10:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_auto_20190513_0838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='unique_id',
            field=models.CharField(default='article_uuid=c4c93a21-df77-4816-862e-54cda7717233', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='articlecol',
            name='unique_id',
            field=models.CharField(default='articlecol_uuid=ee0eecf0-fadf-4c2a-b37f-e3040a072a84', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='unique_id',
            field=models.CharField(default='comment_uuid=a6dd92ed-716a-4fa1-a0b6-8f3ca6110e3e', max_length=128, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='unique_id',
            field=models.CharField(default='reward_uuid=76d5bae2-8816-4166-99a6-cac50e16ff3f', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='unique_id',
            field=models.CharField(default='tag_uuid=ba679cc2-8b6e-40b2-b22a-2a3bfd0f72a4', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='type',
            name='unique_id',
            field=models.CharField(default='type_uuid=756692ea-0872-4f75-9e3e-ba6aad79c9f6', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
    ]
