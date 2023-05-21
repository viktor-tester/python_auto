import requests

token = 'fd14176a7a6acd08b83f2eec7f4c30a0' # Твой токен
url = 'https://pokemonbattle.me:9104'   # Базовый урл

responce_add_pokemon = requests.post (f'{url}/pokemons', headers={'trainer_token' : token}, json={
    "name": "Пикачу",
    "photo": "https://dolnikov.ru/pokemons/albums/025.png"
})

#автоматизируем наш код, сделал сам две строчки, получаем айди нашего покемона и используем дальше в нужных местах.
response_body = responce_add_pokemon.json()
pokemon_id = response_body['id']

print(responce_add_pokemon.text)


change = requests.put (f'{url}/pokemons', headers={'trainer_token' : token}, json={
    "pokemon_id": pokemon_id,
    "name": "vaszw",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
})
print(change.text)

add_pokeboll = requests.post (f'{url}/trainers/add_pokeball', headers={'trainer_token' : token}, json={
    "pokemon_id": pokemon_id
})
print(add_pokeboll.text)