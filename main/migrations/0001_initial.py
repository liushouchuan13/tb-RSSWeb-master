# Generated by Django 2.0.4 on 2018-04-21 06:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RSS',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=128, verbose_name='rss标题')),
                ('link', models.CharField(max_length=512, verbose_name='rss链接')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='添加时间')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='更新时间')),
            ],
        ),
    ]
