# Generated by Django 5.1.4 on 2025-01-20 11:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranking',
            name='game_played',
        ),
        migrations.RemoveField(
            model_name='ranking',
            name='point_taken',
        ),
        migrations.AddField(
            model_name='ranking',
            name='games_played',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='ranking',
            name='points_taken',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='games_drawn',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='games_lost',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='games_won',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ranking',
            name='username',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rankings', to='myapp.student'),
        ),
    ]
