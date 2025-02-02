# Generated by Django 2.2.16 on 2021-05-22 00:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_communities', '0033_auto_20191209_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='community',
            name='about_us',
            field=models.TextField(blank=True, max_length=5000, null=True, verbose_name='about us'),
        ),
        migrations.AddField(
            model_name='community',
            name='area',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='area'),
        ),
        migrations.AddField(
            model_name='community',
            name='department',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='department'),
        ),
        migrations.AddField(
            model_name='community',
            name='employee',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='employee'),
        ),
        migrations.AddField(
            model_name='community',
            name='energy_demand',
            field=models.CharField(blank=True, max_length=40, null=True, verbose_name='energy demand'),
        ),
        migrations.AddField(
            model_name='community',
            name='group_type',
            field=models.CharField(blank=True, choices=[('C', 'City'), ('Q', 'Company'), ('I', 'Institution'), ('U', 'University')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='industry',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='industry'),
        ),
        migrations.AddField(
            model_name='community',
            name='institution',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='institution'),
        ),
        migrations.AddField(
            model_name='community',
            name='location',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='location'),
        ),
        migrations.AddField(
            model_name='community',
            name='population',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='population'),
        ),
        migrations.AddField(
            model_name='community',
            name='website',
            field=models.URLField(blank=True, null=True, verbose_name='website'),
        ),
    ]
