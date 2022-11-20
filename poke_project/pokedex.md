# Pokedex


## BONJOUR !

---



`Un RATTATA sauvage apparaît !`

## Musique

[https://www.youtube.com/watch?v=EkLHogQCXMc](https://www.youtube.com/watch?v=EkLHogQCXMc)



## Fonctionnalités nécessaires

---

[pokemon.csv](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/65b98c95-8b09-4661-be50-7eee57f361d0/pokemon.csv)

### POKEDEX

1. Transformation d’un CSV des Pokémons
    1. Télécharger le CSV POKÉMON
    2. Création d’un model PokedexCreature
        - Il doit contenir tous les champs du CSV
        - chaque instance représente une entrée du POKEDEX
    3. Transformation du CSV en instances du model Pokémon (Django management command)
2. API read-only du model créé (ReadOnlyModelViewSet)
    1. Action LIST
        - `GET /pokedex`
            - Renvoi une sérialisation de toutes les instances concernées
        - On devra pouvoir filtrer optionnellement les Pokémons reçus selon :
            - leur type1
            - leur type2
            - leur génération
            - s'ils sont légendaires
    2. Action RETRIEVE
        - `GET /pokedex/{id}`
            - Renvoi une sérialisation de l’instance visée

### POKEMON

- Créer un model Pokémon, qui représente les individus
- API de CRUD (create read update delete) (ModelViewSet, ModelSerializer)
    - CREATE
        - Un individu fait référence à une entrée du POKEDEX
        - Il peut être sauvage ou non : `trainer_id` est optionnel
        - `surname` est optionnel, par défaut le Pokémon a pour surname le nom de l’entrée du POKEDEX à laquelle il fait référence
        - JSON BODY
            
            ```json
            {
            	"pokedex_creature_id": 1,
            	"trainer_id": null,
            	"surname": "LeSurnomDeMonPokemon",
              "level": 1,
              "experience": 1,
            }
            ```
            
    - ACTION (ViewSet actions)
    - Un utilisateur peut donner de l’expérience à un Pokémon
        - `POST /pokemon/{id}/give-xp`
            
            ```json
            {
            	"amount": 1,
            }
            ```
            
        - Tous les 100 points d’expérience gagnée, le Pokémon gagne un niveau

## BONUS

---

**FUTURES FEATURES **

🔥🔥`GET pokedex/` qui ne renvoi que des informations partielles, et `GET pokedex/{id}` qui renvoi toutes les informations de l’entrée du POKEDEX

🔥 Une page admin permettant la consultation/l’ajout de Pokémon dans le pokedex

🔥🔥 Un dockerfile

🔥🔥🔥 Un docker-compose avec PostgreSQL comme BDD pour Django

Swagger/swagger-like (drf-yasg ou drf-spectacular)

🔥🔥Tests de l’API : les filtres, l’action

🔥 Hébergement de l’API (sur un dédié, un Heroku... ce que tu veux)

🔥 De la pagination

🔥🔥🔥 N’importe quelle autre feature qui te ferait plaisir 🔥🔥🔥

**`ATTRAPONS-LES TOUS !`**