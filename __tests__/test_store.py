import pytest # engine/framework de teste de unidade
import requests #framework de teste de API
import json
from utils.utils import read_csv


order_id = 420665201
order_petId = 420665202
order_quantity = 2
order_shipDate = "2024-06-11T15:41:49.353Z"
order_status = "placed"
order_complete = "true"

url="https://petstore.swagger.io/v2/store/order"

headers={'Content-Type': 'application/json'}

def test_post_order():

    order = open('./fixtures/json/order1.json')
    data = json.loads(order.read())

    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data)
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == order_id
    assert response_body['petId'] == order_petId
    assert response_body['status'] == "placed"

def test_get_order():


    response = requests.get(
        url = f'{url}/{order_id}',
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == order_id
    assert response_body['petId'] == order_petId
    assert response_body['quantity'] == order_quantity

def test_delete_order():

    response = requests.delete(
        url=f'{url}/{order_id}',
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['type'] == 'unknown'
    assert response_body['message'] == f'{order_id}'


@pytest.mark.parametrize('order_id,order_petId,order_quantity,order_shipDate,order_status,order_complete',
                         read_csv('./fixtures/csv/orders.csv'))
def test_post_order_dinamico(order_id,order_petId,order_quantity,order_shipDate,order_status,order_complete):

    order = {}
    order['id'] = int(order_id)
    order['petId'] = int(order_petId)
    order['quantity'] = int(order_quantity)
    order['shipDate'] = order_shipDate
    order['status'] = order_status
    order['complete'] = bool(order_complete)

    order = json.dumps(obj=order, indent=4)
    print('\n' + order)

    response = requests.post(
        url=url,
        headers=headers,
        data=order,

    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == int(order_id)
    assert response_body['petId'] == int(order_petId)
    assert response_body['status'] == order_status






