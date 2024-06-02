import allure
import helper
from data import DataRequest
from stellar_burgers_api import UserApi


class TestChangeUser:
    @allure.title('Проверка изменения данных с авторизацией')
    @allure.description('Отправка PATCH-запроса на изменение данных, проверка статуса и тела ответа')
    def test_changing_user_data_with_authorization_create_and_delete_user_success(self, create_and_delete_user):
        response_create = create_and_delete_user
        token = response_create.json()['accessToken']
        response_change = UserApi.change_user(token, helper.payload)

        assert response_change.status_code == 200 and response_change.json()['success'] is True

    @allure.title('Проверка изменения данных без авторизации')
    @allure.description('Отправка PATCH-запроса на изменение данных, проверка статуса и тела ответа')
    def test_changing_user_data_without_authorization_shows_error(self):
        response_change = UserApi.change_user('', helper.payload)

        assert (response_change.status_code == 401
                and response_change.json()['message'] == DataRequest.WITHOUT_AUTHORIZATION)
