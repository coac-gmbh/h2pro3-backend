# Generated by Django 2.2.5 on 2019-11-26 12:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_notifications', '0021_usernewpostnotification'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usernewpostnotification',
            name='user_notification_subscription',
        ),
    ]
