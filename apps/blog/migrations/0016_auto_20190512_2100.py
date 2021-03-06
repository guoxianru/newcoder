# Generated by Django 2.1.7 on 2019-05-12 21:00

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20190512_2100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('3ae991b5-d1ca-4d49-ac88-f09e9ed55161'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='articlecol',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('5cb84cbc-e1b7-4b41-a787-96b13ab9f2a2'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('f04ff737-8834-4e77-b5bd-c0f649effa96'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('e78be5d7-fdd9-4f7f-a8e1-78972f1978ca'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('618aae3f-b465-4d90-9ee7-fac70e2e2966'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='type',
            name='unique_id',
            field=models.CharField(default=uuid.UUID('6e787b9e-0c34-4980-b8e0-ac17d59e608d'), max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
    ]
