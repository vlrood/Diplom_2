import allure
import helper
from data import DataUser, DataRequest
from stellar_burgers_api import UserApi


class TestLogin:
    @allure.title('Проверка авторизации существующего пользователя')
    @allure.description('Отправка POST-запроса авторизации, проверка статуса и тела ответа')
    def test_login_as_an_existing_user_success(self):
        login_response = UserApi.login_user(DataUser.BODY_LOGIN)

        assert login_response.status_code == 200 and login_response.json()['success'] is True

    @allure.title('Проверка авторизации несуществующего пользователя')
    @allure.description('Отправка POST-запроса авторизации, проверка статуса и тела ответа')
    def test_login_as_an_non_existing_user_shows_error(self):
        login_response = UserApi.login_user(helper.payload)

        assert (login_response.status_code == 401
                and login_response.json()['message'] == DataRequest.NON_EXISTING_USER)
