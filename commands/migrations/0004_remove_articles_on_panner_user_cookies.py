# Generated by Django 3.1.4 on 2020-12-05 12:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('commands', '0003_auto_20201202_1305'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='articles_on_panner',
            name='user_cookies',
        ),
    ]
