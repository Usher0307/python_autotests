import requests

URL = 'https://api.pokemonbattle.ru/v2'
TOKEN = '792a17aebeb617090c5536c4f0f1e859'
HEADER = {'Content-Type' : 'application/json', 'trainer_token': TOKEN}
body_registration = {
    "trainer_token": TOKEN,
    "email": "Usher0307@yandex.ru",
    "password": "030775Eau"
}

body_confirmation = {
    "trainer_token": TOKEN
}
body_create = {
    "name": "Бульбозавр",
    "photo_id": 1
}

body_new_name = {
    "pokemon_id": "129928",
    "name": "Victor",
    "photo_id": 1
}

body_add_pokeball = {
    "pokemon_id": "129928"
}


'''response = requests.post(url = f'{URL}/trainers/reg', headers = HEADER, json = body_registration)

print(response.text)

response_confirmation = requests.post(url = f'{URL}/trainers/confirm_email', headers = HEADER, json = body_confirmation)
print(response_confirmation.text)


response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.text)

response_create = requests.post(url = f'{URL}/pokemons', headers = HEADER, json = body_create)
print(response_create.status_code)

pokemon_id = response_create.json()['id']
print(pokemon_id)'''

response_new_name = requests.put(url = f'{URL}/pokemons', headers = HEADER, json = body_new_name)
print(response_new_name.text)

response_add_pokeball = requests.post(url = f'{URL}/trainers/add_pokeball', headers = HEADER, json = body_add_pokeball)
print(response_add_pokeball.text)