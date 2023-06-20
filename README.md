# Pokedex by Poke Project


I've started this project when doing an interview. The project kind of standstill after the interview (didn't get the job, but that happens). 

Yet the project drew attention with some folks out there. 

After giving some thoughts, I've decided to improve the project and using it as a learning process (I'm a fan of Pokemon, I cannot leave Pika that way!). 

My blue print will be the following 

- Put some VUE JS as front end
- Use the JS to have with the characteristics of the pokemon like [here](https://www.pokemon.com/fr/pokedex/pikachu)

![Pikachu](pikachu.png)

# Howto

How to create a model pokedex and a pokemon model. Everything you want to know on how to create the pokedex and the pokemon model, through this [URL](pokedex.md)

How does the import work?

````bash
# For Linux : 
./manage.py import --path "/home/Andy/poke.csv"
````

````powershell
<# For Windows : #>
python.exe .\manage.py import --path "C:\Users\DELL\Projects\Python\pokemon\poke.csv"



````

How to use the pokedex endpoint?

````
http://127.0.0.1:8000/api/pokemons_list/
````

The pokedex endpoint can be filtered by attributes

````
http://127.0.0.1:8000/api/pokemon_by_attrib/Generations=1
````


How to use the pokemon endpoint?

````
http://127.0.0.1:8000/api/pokemon

````
