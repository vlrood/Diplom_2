import random
import requests
from faker import Faker
import urls
from data import DataUser

fake = Faker()
payload = {
    "email": f'{fake.first_name()}_76_{random.randint(100, 999)}@yandex.ru',
    "password": f'{random.randint(10000, 9999999999)}',
    "name": fake.name()
           }


class TestDataHelper:
    @staticmethod
    def get_random_list_ingredients(count):
        for i in range(count):
            response = requests.get(f'{urls.BASE_URL}{urls.INGREDIENTS}')

            return response.json()['data'][i]['_id']

    @staticmethod
    def modify_user_body(key, value):
        body = DataUser.BODY_USER
        body[key] = value

        return body
