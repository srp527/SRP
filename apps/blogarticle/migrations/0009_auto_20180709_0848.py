# Generated by Django 2.0.5 on 2018-07-09 08:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogarticle', '0008_auto_20180625_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogarticle.Category', verbose_name='文章类别'),
        ),
    ]
