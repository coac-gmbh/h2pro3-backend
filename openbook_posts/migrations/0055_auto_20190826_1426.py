# Generated by Django 2.2.4 on 2019-08-26 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_posts', '0054_auto_20190826_1402'),
    ]

    operations = [
        migrations.AlterField(
            model_name='postvideo',
            name='thumbnail_height',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
        migrations.AlterField(
            model_name='postvideo',
            name='thumbnail_width',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
    ]
