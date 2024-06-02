class DataUser:
    BODY_USER = {
        'email': 'test_lera@yandex.ru',
        'password': f'276543987653212',
        'name': 'Test'

    }
    BODY_LOGIN = {
        'email': 'test_lera@yandex.ru',
        'password': f'276543987653212'
    }


class DataRequest:
    WITH_AUTHORIZED_USER = 'User already exists'
    WITHOUT_EMAIL = 'Email, password and name are required fields'
    NON_EXISTING_USER = 'email or password are incorrect'
    WITHOUT_AUTHORIZATION = 'You should be authorised'
    WITHOUT_INGREDIENTS = 'Ingredient ids must be provided'
    ORDER_WITHOUT_AUTHORIZATION = 'You should be authorised'


class DataOrder:
    FLUORESCENT_BURGER = 'Флюоресцентный бургер'
    BODY_2 = ["61c0c5a71d1f82001bdaaa6d4", "61c0c5a71d1f82001bdaaa6d2"]
