import allure
import helper
from data import DataOrder, DataRequest
from stellar_burgers_api import OrderApi


class TestCreateOrder:
    @allure.title('Проверка успешного создания заказа авторизованного пользователя')
    @allure.description('Отправка POST-запроса на создание заказа, проверка статуса и тела ответа')
    def test_create_order_with_authorization_create_and_delete_user_success(self, create_and_delete_user):
        user = create_and_delete_user
        token = user.json()['accessToken']
        ingredients = helper.TestDataHelper.get_random_list_ingredients(3)
        order_response = OrderApi.create_order(ingredients, token)

        assert order_response.status_code == 200

    @allure.title('Проверка успешного создания заказа неавторизованного пользователя')
    @allure.description('Отправка POST-запроса на создание заказа, проверка статуса и тела ответа')
    def test_create_order_without_authorization_success(self):
        ingredients = helper.TestDataHelper.get_random_list_ingredients(2)
        order_response = OrderApi.create_order(ingredients, '')

        assert order_response.status_code == 200 and order_response.json()['success'] is True

    @allure.title('Проверка ошибки заказа без ингредиентов')
    @allure.description('Отправка POST-запроса на создание заказа без ингредиентов, проверка статуса и тела ответа')
    def test_create_order_without_ingredients_shows_error(self):
        order_response = OrderApi.create_order([], '')

        assert order_response.status_code == 400 and order_response.json()['message'] == DataRequest.WITHOUT_INGREDIENTS

    @allure.title('Проверка ошибки заказа ингредиентов с неверным хэшем')
    @allure.description('Отправка POST-запроса на создание заказа, проверка статуса ответа')
    def test_create_order_without_invalid_hash_shows_error(self):
        order_response = OrderApi.create_order(DataOrder.BODY_2, '')

        assert order_response.status_code == 500
