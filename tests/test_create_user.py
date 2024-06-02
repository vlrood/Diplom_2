import allure
from data import DataRequest, DataUser
import helper
from stellar_burgers_api import UserApi


class TestCreateUser:
    @allure.title('Проверка успешного создания пользователя')
    @allure.description('Отправка POST-запроса на создание пользователя, проверка статуса и тела ответа')
    def test_create_user_create_and_delete_user_success(self, create_and_delete_user):
        user_response = create_and_delete_user

        assert user_response.status_code == 200 and user_response.json()['success'] is True

    @allure.title('Проверка невозможности создания пользователя, который уже зарегистрирован;')
    @allure.description('Отправка двух POST-запросов на создание пользователя, проверка статуса и тела ответа')
    def test_create_authorized_user_shows_error(self):
        UserApi.create_user(DataUser.BODY_USER)
        user_response = UserApi.create_user(DataUser.BODY_USER)

        assert (user_response.status_code == 403
                and user_response.json()['message'] == DataRequest.WITH_AUTHORIZED_USER)

    @allure.title('Проверка невозможности создания пользователя без обязательных полей')
    @allure.description('Отправка POST-запроса без почты, проверка статуса и тела ответа')
    def test_create_user_without_email(self):
        payload = helper.TestDataHelper.modify_user_body('email', '')
        user_response = UserApi.create_user(payload)

        assert user_response.status_code == 403 and user_response.json()['message'] == DataRequest.WITHOUT_EMAIL
