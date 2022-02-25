from statistics import mode
from django.db import models

# Create your models here.


class PokedexCreature(models.Model):
    """
    Store toutes les données du CSV fournis
    dans le modele PokeDexCreature
    """

    Name = models.CharField(max_length=30)
    Type_1 = models.CharField(max_length=20, db_column="Type 1")
    Type_2 = models.CharField(max_length=20, db_column="Type 2")
    Total = models.IntegerField()
    HP = models.IntegerField()
    Attack = models.IntegerField()
    Defense = models.IntegerField()
    Sp_Atk = models.IntegerField(db_column="Sp. Atk")
    Sp_Def = models.IntegerField(db_column="Sp. Def")
    Speed = models.IntegerField()
    Generation = models.IntegerField()
    Legendary = models.CharField(max_length=20)


class Pokemon(models.Model):
    """
    Un individu fait référence à
    une entrée du POKEDEX
    """

    pokedex_creature_id = models.IntegerField(primary_key=True)
    trainer_id = models.IntegerField(null=True)
    surname = models.CharField(max_length=30)
    level = models.IntegerField()
    experience = models.IntegerField()
    amount = models.IntegerField(null=True)
