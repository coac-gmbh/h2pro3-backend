# Generated by Django 2.2.16 on 2021-10-13 15:57

from django.conf import settings
from django.db import migrations, models
import imagekit.models.fields
import openbook_communities.helpers


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_communities', '0037_community_closed'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='community',
            name='about_us',
        ),
        migrations.AlterField(
            model_name='community',
            name='avatar',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=openbook_communities.helpers.upload_to_community_avatar_directory, verbose_name='avatar'),
        ),
        migrations.AlterField(
            model_name='community',
            name='cover',
            field=imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to=openbook_communities.helpers.upload_to_community_cover_directory, verbose_name='cover'),
        ),
        migrations.AlterField(
            model_name='community',
            name='description',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='description'),
        ),
        migrations.AlterField(
            model_name='community',
            name='rules',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='rules'),
        ),
        migrations.AlterField(
            model_name='community',
            name='starrers',
            field=models.ManyToManyField(blank=True, related_name='favorite_communities', to=settings.AUTH_USER_MODEL),
        ),
    ]
