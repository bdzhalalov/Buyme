import os

import pytest
from payment.models import Item
from rest_framework.test import APIClient


@pytest.fixture()
def client():
    client = APIClient()
    return client


@pytest.fixture()
def item():
    item = Item.objects.create(
        name='Test item',
        description='Test description',
        price=3000,
        currency='usd'
    )
    return {'id': item.id, 'name': item.name, 'description': item.description, 'price': item.price, 'currency': item.currency}


@pytest.fixture()
def item_by_id(item):
    item_by_id = item
    return item_by_id['id']

