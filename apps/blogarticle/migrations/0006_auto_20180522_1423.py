# Generated by Django 2.0.5 on 2018-05-22 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogarticle', '0005_auto_20180520_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='tag',
            field=models.CharField(default='', max_length=20, verbose_name='文章标签'),
        ),
    ]
