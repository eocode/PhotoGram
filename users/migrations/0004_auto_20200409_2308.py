# Generated by Django 3.0.5 on 2020-04-10 04:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20200407_1613'),
    ]

    operations = [
        migrations.CreateModel(
            name='Follow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('follower', models.IntegerField(default=0)),
                ('following', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='profile',
            name='posts_count',
            field=models.IntegerField(default=0),
        ),
    ]
