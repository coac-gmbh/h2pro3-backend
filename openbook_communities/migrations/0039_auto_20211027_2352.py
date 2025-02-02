# Generated by Django 2.2.16 on 2021-10-27 22:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_communities', '0038_auto_20211013_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='community',
            name='group_type',
            field=models.CharField(blank=True, choices=[('C', 'City'), ('Q', 'Company'), ('I', 'Institution'), ('U', 'Research'), ('P', 'Project'), ('E', 'Event')], max_length=1, null=True),
        ),
        migrations.AddField(
            model_name='community',
            name='project_duration',
            field=models.CharField(blank=True, max_length=64, null=True, verbose_name='project duration'),
        ),
        migrations.AddField(
            model_name='community',
            name='project_partners',
            field=models.TextField(blank=True, null=True, verbose_name='project partners'),
        ),
        migrations.AddField(
            model_name='community',
            name='lessons_learned',
            field=models.TextField(blank=True, null=True, verbose_name='lessons learned'),
        ),
    ]
