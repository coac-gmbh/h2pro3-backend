# Generated by Django 2.1.5 on 2019-02-09 15:31

from django.db import migrations
import imagekit.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_auth', '0012_merge_20181207_1647'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(null=True, upload_to='', verbose_name='avatar'),
        ),
    ]
