# Generated by Django 3.1.2 on 2020-10-22 00:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quipi', '0003_prompt_quip'),
    ]

    operations = [
        migrations.RenameField(
            model_name='quip',
            old_name='times_player',
            new_name='times_played',
        ),
    ]
