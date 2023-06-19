# Generated by Django 4.0.2 on 2023-06-19 11:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PokedexCreature',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Poke_Name', models.CharField(max_length=255)),
                ('Type_1', models.CharField(blank=True, max_length=50, null=True)),
                ('Type_2', models.CharField(blank=True, max_length=50, null=True)),
                ('Total', models.PositiveIntegerField()),
                ('HP', models.PositiveIntegerField()),
                ('Attack', models.PositiveIntegerField()),
                ('Defense', models.PositiveIntegerField()),
                ('Sp_Atk', models.PositiveIntegerField()),
                ('Sp_Def', models.PositiveIntegerField()),
                ('Speed', models.PositiveIntegerField()),
                ('Generation', models.PositiveIntegerField()),
                ('Legendary', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Last_name', models.CharField(max_length=255)),
                ('First_name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Trainer', models.CharField(blank=True, max_length=125, null=True)),
                ('Poke_Trainer_Nickname', models.CharField(blank=True, max_length=255, null=True)),
                ('Level', models.PositiveIntegerField()),
                ('Experience', models.IntegerField()),
                ('Amount', models.IntegerField(null=True)),
                ('pokedex_creature_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poke_api.pokedexcreature')),
            ],
        ),
    ]
