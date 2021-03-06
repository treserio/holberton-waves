# Generated by Django 4.0.4 on 2022-05-19 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='videos',
            name='topic',
            field=models.TextField(null=True),
        ),
        migrations.AddField(
            model_name='videos',
            name='updated',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='author',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='author_pic_url',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='description',
            field=models.TextField(null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='duration',
            field=models.DurationField(null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='likes',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='published',
            field=models.CharField(max_length=23, null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='thumbnail',
            field=models.URLField(null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='title',
            field=models.CharField(max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='videos',
            name='views',
            field=models.BigIntegerField(null=True),
        ),
    ]
