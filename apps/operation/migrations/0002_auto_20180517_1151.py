# Generated by Django 2.0.5 on 2018-05-17 11:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlereplycomments',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='目标用户ID'),
        ),
        migrations.AlterField(
            model_name='articlereplycomments',
            name='user',
            field=models.IntegerField(default=0, verbose_name='用户ID'),
        ),
    ]
