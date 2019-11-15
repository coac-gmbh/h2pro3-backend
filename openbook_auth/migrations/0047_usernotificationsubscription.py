# Generated by Django 2.2.5 on 2019-11-15 13:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('openbook_auth', '0046_usernotificationssettings_community_new_post_notifications'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNotificationSubscription',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subscriber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_notification_subscriptions', to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='notification_subscribers', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('user', 'subscriber')},
            },
        ),
    ]
