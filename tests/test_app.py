from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app

cliente = TestClient(app)


def test_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # Organização

    response = client.get('/')  # Ação

    assert response.status_code == HTTPStatus.OK  # Verificação
    assert response.json() == {'message': 'Olá Mundo!'}
