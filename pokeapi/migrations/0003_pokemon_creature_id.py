# Generated by Django 4.1.6 on 2023-02-14 16:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pokeapi', '0002_pokemon_generation_pokemon_legendary'),
    ]

    operations = [
        migrations.AddField(
            model_name='pokemon',
            name='creature_id',
            field=models.IntegerField(help_text='ID number assigned by Kaggle.', null=True),
        ),
    ]