# Generated by Django 2.1.7 on 2019-05-13 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0021_auto_20190513_1134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='unique_id',
            field=models.CharField(default='article_uuid=686341a5-600c-4663-be30-d26f01b397b2', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='articlecol',
            name='unique_id',
            field=models.CharField(default='articlecol_uuid=0e9da4a1-83d3-4ccd-8dad-536aa074b4b8', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='parent',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='blog.Comment', verbose_name='被评论用户'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='unique_id',
            field=models.CharField(default='comment_uuid=64812f80-90e2-4c4c-a8ff-e6ce5ca20101', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='reward',
            name='unique_id',
            field=models.CharField(default='reward_uuid=27348a3d-3644-454d-b317-8c97280122e0', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='tag',
            name='unique_id',
            field=models.CharField(default='tag_uuid=1ec3b20c-5f78-41b7-800f-45b770b261af', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
        migrations.AlterField(
            model_name='type',
            name='unique_id',
            field=models.CharField(default='type_uuid=69d8a9aa-4529-41cf-b20c-beef54dff57c', max_length=128, unique=True, verbose_name='唯一标识符'),
        ),
    ]
