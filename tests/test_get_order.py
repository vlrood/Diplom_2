import allure
from data import DataRequest
from helper import TestDataHelper
from stellar_burgers_api import OrderApi


class TestGetOrder:
    @allure.title('Проверка успешного получения заказов авторизованного пользователя')
    @allure.description('Отправка GET-запроса на получение заказов, проверка статуса и тела ответа')
    def test_get_order_existing_user_create_and_delete_user_success(self, create_and_delete_user):
        user = create_and_delete_user
        token = user.json()['accessToken']
        ingredients = TestDataHelper.get_random_list_ingredients(5)
        OrderApi.create_order(ingredients, token)
        response_get_order = OrderApi.get_order(token)

        assert response_get_order.status_code == 200 and 'orders' in response_get_order.json()

    @allure.title('Проверка ошибки получения заказов неавторизованного пользователя')
    @allure.description('Отправка GET-запроса на получение заказов, проверка статуса и тела ответа')
    def test_get_order_non_existing_user_shows_error(self):
        response_get_order = OrderApi.get_order('')

        assert (response_get_order.status_code == 401
                and response_get_order.json()['message'] == DataRequest.ORDER_WITHOUT_AUTHORIZATION)
