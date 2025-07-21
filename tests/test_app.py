from http import HTTPStatus


def test_root_deve_retornar_ok_e_ola_mundo(client):
    response = client.get('/')  # Ação

    assert response.status_code == HTTPStatus.OK  # Verificação
    assert response.json() == {'message': 'Olá Mundo!'}


def test_create_user(client):
    response = client.post(
        '/users/',
        json={
            'username': 'test_username',
            'email': 'email@test.com',
            'password': 'test_password',
        },
    )

    assert response.status_code == HTTPStatus.CREATED  # Verificação
    assert response.json() == {
        'id': 1,
        'username': 'test_username',
        'email': 'email@test.com',
    }


def test_read_users(client):
    response = client.get('/users/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'users': [
            {
                'username': 'test_username',
                'email': 'email@test.com',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'test_username',
            'email': 'email@test.com',
            'password': 'password',
        },
    )
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {
        'username': 'test_username',
        'email': 'email@test.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'User deleted'}
