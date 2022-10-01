from statistics import mode
from django.db import models

class PokedexCreature(models.Model):
    Poke_id = models.IntegerField()
    Poke_Name = models.CharField(max_length=255)
    Type_1 = models.CharField(choices=("cle","valeur"))
    Type_2 = models.CharField(choices=("cle","valeur"),null=True,blank=True)
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
    Pokedex_type = models.ForeignKey(on_delete=models.CASCADE)
    #question à se poser si l'entraîneur lâche l'affaire, que se passe t'il 
    #pour le pokemon ? Il redevient sauvage ou il meurt T_T
    Trainer= models.ForeignKey(null=True,on_delete=models) 
    Poke_Trainer_Nickname = models.CharField(max_length=255,null=True,blank=True)
    Level = models.PositiveIntegerField()
    Experience = models.IntegerField()
    Amount = models.IntegerField(null=True)

    @property
    def Surname(self):
        return self.Poke_Trainer_Nickname if self.Poke_Trainer_Nickname else self.Pokedex_type.Poke_name

    
