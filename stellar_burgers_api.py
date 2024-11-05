import requests
import urls
import allure


class UserApi:
    @staticmethod
    @allure.step('Отправка POST-запроса на создание пользователя')
    def create_user(body):
        return requests.post(f'{urls.BASE_URL}{urls.CREATE_USER_PATH}', data=body)

    @staticmethod
    @allure.step('Отправка POST-запроса на авторизацию')
    def login_user(body):
        return requests.post(f'{urls.BASE_URL}{urls.USER_LOGIN_PATH}', json=body)

    @staticmethod
    @allure.step('Отправка PATCH-запроса на изменение пользователя')
    def change_user(token, body):
        return requests.patch(f'{urls.BASE_URL}{urls.CHANGE_USER_PATH}', json=body, headers={'Authorization': token})

    @staticmethod
    @allure.step('Отправка DELETE-запроса на удаление пользователя')
    def delete_user(token):
        requests.delete(f'{urls.BASE_URL}{urls.DELETE_USER}', headers={'Authorization': token})


class OrderApi:
    @staticmethod
    @allure.step('Отправка POST-запроса на создание заказа')
    def create_order(body, token):
        return requests.post(f'{urls.BASE_URL}{urls.CREATE_ORDER_PATH}', json={"ingredients": body},
                             headers={'Authorization': token})

    @staticmethod
    @allure.step('Отправка GET-запроса на получение заказов конкретного пользователя')
    def get_order(token):
        return requests.get(f'{urls.BASE_URL}{urls.GET_ORDER_PATH}', headers={'Authorization': token})