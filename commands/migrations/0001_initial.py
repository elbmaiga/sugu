# Generated by Django 3.1.4 on 2020-12-02 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_name', models.CharField(blank=True, max_length=40, verbose_name='Last name')),
                ('first_name', models.CharField(blank=True, max_length=40, verbose_name='First name')),
                ('email', models.EmailField(max_length=30, unique=True, verbose_name='Email')),
                ('telephone', models.CharField(max_length=20, unique=True, verbose_name='Telephone')),
                ('address', models.TextField(blank=True, verbose_name='Address')),
            ],
        ),
        migrations.CreateModel(
            name='Panner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.SmallIntegerField(default=1, verbose_name='Quantity')),
                ('user_cookies', models.CharField(max_length=255, unique=True, verbose_name='User cookies')),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.articles')),
            ],
        ),
        migrations.CreateModel(
            name='Commands',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('deliverance', models.BooleanField(default=False, verbose_name='With deliverance ?')),
                ('status', models.BooleanField(default=False, verbose_name='is Done ?')),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='Created at')),
                ('client', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commands.client')),
                ('panner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commands.panner')),
            ],
        ),
    ]
