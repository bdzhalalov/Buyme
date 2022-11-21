import pytest


@pytest.mark.django_db
def test_item(item):
    test_item = item
    assert test_item['id'] == 1
    assert test_item['name'] == 'Test item'
    assert test_item['description'] == 'Test description'
    assert test_item['price'] == 3000
    assert test_item['currency'] == 'usd'


@pytest.mark.django_db
def test_get_items(client):
    response = client.get('')
    assert response.status_code == 200


@pytest.mark.django_db
def test_invalid_get_items(client):
    response = client.get('/items')
    assert response.status_code == 404


@pytest.mark.django_db
def test_get_item_by_id(client, item_by_id):
    response = client.get('/item/' + str(item_by_id))
    assert response.status_code == 200


@pytest.mark.django_db
def test_invalid_get_item_by_id(client):
    response = client.get('/item/3')
    assert response.status_code == 404


@pytest.mark.django_db
def test_buy_item_by_id(client, item_by_id):
    response = client.post('/buy/' + str(item_by_id))
    assert response.status_code == 200


@pytest.mark.django_db
def test_invalid_method_buy_item_by_id(client, item_by_id):
        response = client.get('/buy/' + str(item_by_id))
        assert response.status_code == 405
