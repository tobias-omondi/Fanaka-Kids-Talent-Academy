# Generated by Django 5.1.6 on 2025-02-11 11:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_ranking_game_played_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='event_date',
            field=models.TextField(default='exit', max_length=20),
            preserve_default=False,
        ),
    ]
