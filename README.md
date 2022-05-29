# Pokedex by Poke Project


I've started this project when doing an interview. The project kind of standstill after the interview (didn't get the job, but that happens). 

Yet the project drew attention with some folks out there. 

After giving some thoughts, I've decided to improve it and using oit as a learning process (I'm a fan of Pokemon, so I cannot leave the project that way). 

My blue print will be the following 

- Put some VUE JS as front end
- Use the JS to have with the characteristics of the pokemon like [here](https://www.pokemon.com/fr/pokedex/pikachu)

![Pikachu](pikachu.png)

# Howto

How to create a model pokedex and a pokemon model. Everything you want to know on how to create the pokedex and the pokemon model, through this [URL](https://wirehaired-moonstone-c71.notion.site/Test-technique-back-end-Pokedex-6d1f91bdbf6643bc87e23722af1176ab)

How does the import work?

````python

./manage.py import 

type path of the csv file and csv file name, don't put quotation mark for path
/home/andykw/projects/python/poke_project/poke_project/poke.csv

````

How to use the pokedex endpoint?

````
http://127.0.0.1:8000/pokedex/
````

The pokedex endpoint can be filtered by individual

````
http://127.0.0.1:8000/pokedex/1
````

How to filter the pokedex with the conditions?

````
http://127.0.0.1:8000/pokedex/?Generation=1
````


How to use the pokemon endpoint?

````
http://127.0.0.1:8000/pokemon

````
