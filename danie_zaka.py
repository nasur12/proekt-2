# Насур Сулейманов 22а инженер по тестированию расширенный 
import configuration
import requests
import data
from sender_stand_request import create_order, get_order  # Импорт функций из файла sender_stand_request.py

# Автотест
def test_order_creation_and_retrieval():
    # Создание заказа
    response = create_order(data.order_body)
    assert response.status_code == 201, f"Ошибка создания заказа: {response.status_code}"

    track_number = response.json()["track"]
    print("Заказ создан. Номер трека:", track_number)

    # Получение данных заказа по треку
    order_response = get_order(track_number)

    # Проверки
    assert order_response.status_code == 200, f"Ошибка получения заказа: {order_response.status_code}"
    order_data = order_response.json()

    print("Данные заказа:")
    print(order_data)