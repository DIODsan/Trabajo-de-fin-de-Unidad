import requests
import json

print(                             ''' --------- MENU POKÉMON ----------

1. Ver lista de pokémos por generación.
2. Listar pokemons por forma. Se ingresa alguna forma (deben sugerir valores) y se listan todos los pokemons respectivos.
3. Listar pokemons por habilidad. Se deben sugerir opciones a ingresar para interactuar.
4. Listar pokemons por habitat. Se deben sugerir opciones a ingresar para interactuar.
5. Ver lista de pokémons segun el tipo.

''')

opcion=int(input("Eliga una opcion : " ))

if opcion == 1 : 
    
    id = int(input("Escribe el id de la generacion de pokemon a listar: "))
  
elif opcion==2:
    pass
elif opcion==3:
      print(''' Pokemon segun sus habilidades: 
      1. hedor 
      2. llovizna 
      3. Impulso
      4. armadura de batalla 
      5. robustez
      6. Humedad 
      7. Flexibilidad
      8. Velo arena
      9. Electricidad estatica
     10. Absorbe electricidad
     11. Absorbe agua 
     12. Despiste
     13. Aclimatacion 
     14. Ojo compuesto
     15. Insomnio
     16. Cambio color
     17. Inmunidad
     18. Absorbe fuego 
     19. Polvo escudo
     20. Ritmo propio
      ''')
      ab=int(input("Pokemon segun la habilidad: "))
elif opcion ==4:
    pass
elif opcion ==5:

    print('''Existen diferentes tipos de pokemon como : 
     1. Normal
     2. Peleador
     3. Volador 
     4. Veneno 
     5. Terrestre 
     6. Roca 
     7. Insecto
     8. Fantasma 
     9. Acero
     10. Fuego
     11. Agua 
     12. Planta 
     13. Electrico
     14. Psíquico
     15. Hielo
     16. Dragon 
     17. Siniestro
     18. Hada 

     Marcar segun el indice
     
     ''')
    ti = int(input("Tipo de Pokemon : "))
    
else:
    print("Opcion Invalidad")

def get_generation(id):
    url = f'https://pokeapi.co/api/v2/generation/{id}'


    response = requests.get(url)

    if response.status_code == 200:
    
        data = response.json()
        #print(data)
        results = data['pokemon_species']
        
        if results: 
            for pokemon in results:
                name = pokemon['name']
                print(name)

get_generation(id)

def get_ability(ab):
    url = f'https://pokeapi.co/api/v2/ability/{ab}'

    response = requests.get(url)

    if response.status_code == 200:
    
        data = response.json()
    
        results = data['pokemon']
        
        if results: 
            for pokemon in results:
                name = pokemon['pokemon']['name']
                print(name)

get_ability(ab)

def get_tipo(ti):
    url = f'https://pokeapi.co/api/v2/type/{ti}'

    response = requests.get(url)

    if response.status_code == 200:
    
        data = response.json()
    
        results = data['pokemon']
        
        if results: 
            for pokemon in results:
                name = pokemon['pokemon']['name']
                print(name)
get_tipo(ti)