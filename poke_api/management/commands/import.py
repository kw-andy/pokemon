import csv

from os import getenv

from django.core.management.base import BaseCommand, CommandError
from poke_api.models import PokedexCreature as Pokedex

#PATH_VAL = input(
#    "type path of the csv file and csv file name, don't put quotation mark for path\n"
#)


class Command(BaseCommand):
    help = "Import the csv data and create instances in the model PokedexCreature"

    def add_arguments(self, parser):
        parser.add_argument("--path", nargs="+", type=str, default=1)

    def handle(self, *args, **options):
        try:
            path_file = options["path"][0]
            print(path_file)
            with open(path_file) as csvfile:
                reader = csv.DictReader(csvfile)
                print(reader)
                for line in reader:
                    Name = line["Name"]
                    Type_1 = line["Type 1"]
                    Type_2 = line["Type 2"]
                    Total = line["Total"]
                    HP = line["HP"]
                    Attack = line["Attack"]
                    Defense = line["Defense"]
                    Sp_Atk = line["Sp. Atk"]
                    Sp_Def = line["Sp. Def"]
                    Speed = line["Speed"]
                    Generation = line["Generation"]
                    Legendary = line["Legendary"]

                    with_data_pokedex = Pokedex(
                        Poke_Name=Name,
                        Type_1=Type_1,
                        Type_2=Type_2,
                        Total=Total,
                        HP=HP,
                        Attack=Attack,
                        Defense=Defense,
                        Sp_Atk=Sp_Atk,
                        Sp_Def=Sp_Def,
                        Speed=Speed,
                        Generation=Generation,
                        Legendary=Legendary,
                    )
                    with_data_pokedex.save()
        except Exception as e:
            raise CommandError(e)
