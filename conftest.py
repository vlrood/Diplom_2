import pytest
import requests
import helper
import urls


@pytest.fixture(scope='function')
def create_and_delete_user():
    body = helper.payload
    response = requests.post(f'{urls.BASE_URL}{urls.CREATE_USER_PATH}', json=body)

    yield response

    token = response.json()['accessToken']
    requests.delete(f'{urls.BASE_URL}{urls.DELETE_USER}', headers={'Authorization': token})

