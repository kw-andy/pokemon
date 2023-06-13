from statistics import mode
from django.db import models


class PokedexCreature(models.Model):
    Poke_Name = models.CharField(max_length=255)
    Type_1 = models.CharField(max_length=50, null=True, blank=True)
    Type_2 = models.CharField(max_length=50, null=True, blank=True)
    Total = models.PositiveIntegerField()
    HP = models.PositiveIntegerField()
    Attack = models.PositiveIntegerField()
    Defense = models.PositiveIntegerField()
    Sp_Atk = models.PositiveIntegerField()
    Sp_Def = models.PositiveIntegerField()
    Speed = models.PositiveIntegerField()
    Generation = models.PositiveIntegerField()
    Legendary = models.BooleanField()


class Trainer(models.Model):
    Last_name = models.CharField(max_length=255)
    First_name = models.CharField(max_length=255)


class Pokemon(models.Model):
    pokedex_creature_id = models.ForeignKey('PokedexCreature',
                                     on_delete=models.CASCADE,
                                     )
    Trainer = models.CharField(max_length=125, null=True, blank=True)
    Poke_Trainer_Nickname = models.CharField(max_length=255, null=True, blank=True)
    Level = models.PositiveIntegerField()
    Experience = models.IntegerField()
    Amount = models.IntegerField(null=True)

    @property
    def Surname(self):
        return self.Poke_Trainer_Nickname if self.Poke_Trainer_Nickname \
            else self.Pokedex_type.Poke_name

    
