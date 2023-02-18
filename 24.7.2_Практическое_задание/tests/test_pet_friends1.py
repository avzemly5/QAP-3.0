from api import PetFriends
from settings import valid_email, valid_password
import os

ptFnd = PetFriends()


def test_get_api_key_for_valid_user(email=valid_email, password=valid_password):
    """Проверка того, что запрос API-ключа возвращает статус '200' и что результат содержит слово 'key'"""

    # Отправка запроса и сохранение полученного ответа с кодом статуса в 'status' и текста ответа - в 'result'
    status, result = ptFnd.get_api_key(email, password)

    # Сопоставление полученных данных с ожидаемым результатом
    assert status == 200
    assert 'key' in result


def test_get_all_pets_with_valid_key(filter=''):
    """Проверка того, что запрос всех питомцев возвращает не пустой список.
    Перед этим происходит получение API-ключа и его сохранение в переменную 'auth_key'.
    Затем, при помощи этого ключа, происходит запрос списка всех питомцев и проверка того, что список не пустой.
    Доступное значение параметра 'filter' - 'my_pets' или ''"""

    _, auth_key = ptFnd.get_api_key(valid_email, valid_password)
    status, result = ptFnd.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0


def test_add_new_pet_with_valid_data(name='Патрик', animal_type='Зебра уютная',
                                     age='6', pet_photo='images/cat1.jpg'):
    """Проверка того, что добавление питомца с корректными данными осуществляется"""

    # Получение полного пути изображения питомца и его сохранение в переменную 'pet_photo'
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрос API-ключа и его сохранение в переменую 'auth_key'
    _, auth_key = ptFnd.get_api_key(valid_email, valid_password)

    # Добавление питомца
    status, result = ptFnd.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сопоставление полученных данных с ожидаемым результатом
    assert status == 200
    assert result['name'] == name


def test_successful_delete_own_pet():
    """Проверка возможности удаления 'своего питомца'"""

    # Получение API-ключа 'auth_key' и запрос списка 'своих питомцев'
    _, auth_key = ptFnd.get_api_key(valid_email, valid_password)
    _, my_pets = ptFnd.get_list_of_pets(auth_key, 'my_pets')

    # Если список 'своих питомцев' пустой, происходит добавление нового и повторный запрос списка 'своих питомцев'
    if len(my_pets['pets']) == 0:
        ptFnd.add_new_pet(auth_key, 'Homa', '111', '4', 'images/P1040103.jpg')
        _, my_pets = ptFnd.get_list_of_pets(auth_key, 'my_pets')

    # Берется id первого питомца из списка и отправляется запрос на удаление
    pet_id = my_pets['pets'][0]['id']
    status, _ = ptFnd.delete_pet(auth_key, pet_id)

    # Повторный запрос списка 'своих питомцев'
    _, my_pets = ptFnd.get_list_of_pets(auth_key, 'my_pets')

    # Проверка того, что статус ответа = 200 и что в списке 'своих питомцев' нет id удаленного питомца
    assert status == 200
    assert pet_id not in my_pets.values()


def test_successful_update_own_pet_info(name='Патрик', animal_type='Зебра уютная', age=6):
    """Проверка возможности обновления информации о 'своем питомце'"""

    # Получение API-ключа 'auth_key' и списка 'своих питомцев'
    _, auth_key = ptFnd.get_api_key(valid_email, valid_password)
    _, my_pets = ptFnd.get_list_of_pets(auth_key, 'my_pets')

    # Если список 'своих питомцев' не пустой, происходит обновление имени, типа и возраста питомца
    if len(my_pets['pets']) > 0:
        status, result = ptFnd.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверка того, что статус ответа = '200' и что имя питомца соответствует заданному
        assert status == 200
        assert result['name'] == name
    else:
        # Если список 'своих питомцев' пустой, всплывает исключение с текстом об отсутствии 'своих питомцев'
        raise Exception('There is no my pets')
