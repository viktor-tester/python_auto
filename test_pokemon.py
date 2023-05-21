import requests
import pytest

#тест на проверку статус кода 201 при создание покемона
def test_status_code_create_pokemon():
    token = 'fd14176a7a6acd08b83f2eec7f4c30a0' 
    response = requests.post('https://pokemonbattle.me:9104/pokemons', headers={'trainer_token': token}, json={
    "name": "Бульбазавр",
    "photo": "https://dolnikov.ru/pokemons/albums/025.png"
})
    assert response.status_code == 201

#тест на проверку статус кода 200 при отправке запроса, и при получение нужных данных
def test_trainer_name():
    response = requests.get('https://pokemonbattle.me:9104/trainers', params={'trainer_id': 4267})
    response_body = response.json()
    assert response.status_code == 200
    assert response_body['trainer_name'] == 'Виктор'
