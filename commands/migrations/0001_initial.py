# Generated by Django 3.0 on 2020-12-10 23:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('articles', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Panner_Articles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField(default=1, verbose_name='Quantity')),
                ('articles', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='articles.Articles')),
            ],
        ),
        migrations.CreateModel(
            name='Panner',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_cookies', models.CharField(max_length=255, unique=True, verbose_name='User cookies')),
                ('panner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='commands.Panner_Articles')),
            ],
        ),
    ]