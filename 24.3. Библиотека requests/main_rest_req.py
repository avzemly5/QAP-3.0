import requests
import json
from data import data
from data import headers
from data import pets_1
from data import pets_2

# POST-запрос
r_1 = requests.post(f'https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(data))

print(r_1.status_code)
print('Код ответа - 200\nПитомец создан\n')
pets_id = dict(r_1.json())['id']

data['id'] = pets_id
data['name'] = pets_2


# PUT-запрос
r_2 = requests.put(f'https://petstore.swagger.io/v2/pet', headers=headers, data=json.dumps(data))

print(r_2.status_code)
print(f'Код ответа - 200\nИмя питомца "{pets_1}" изменено на "{pets_2}"')
print('\nЗапрос с сервера данных о питомце по id - ' + str(pets_id))


# GET-запрос
r_3 = requests.get(f'https://petstore.swagger.io/v2/pet/{pets_id}', headers=headers)

print(r_3.status_code)
print('Код ответа - 200 \nНа сервере имеются данные')
print('\nУдаление данных о питомце по id - ' + str(pets_id))


# DELETE-запрос
r_4 = requests.delete(f'https://petstore.swagger.io/v2/pet/{pets_id}', headers=headers)

print(r_4.status_code)
print('Код ответа - 200 \nС сервера удалены данные о питомце')
print('\nПовторный запрос с сервера данных о питомце по id - ' + str(pets_id))


# Повторный GET-запрос
r_5 = requests.get(f'https://petstore.swagger.io/v2/pet/{pets_id}', headers=headers)

print(r_5.status_code)
print('Код ответа - 404 \nНа сервере нет данных о питомце')
