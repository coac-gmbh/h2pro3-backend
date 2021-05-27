# Generated by Django 2.2.16 on 2021-05-27 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_communities', '0036_auto_20210525_2221'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='closed',
            field=models.BooleanField(default=False, help_text='only administrators can publish on closed groups', verbose_name='closed group'),
        ),
    ]
