import pytest
import requests
import json
from utils.utils import read_csv

id_user = 420665201
username_user = "jeh432"
firstName_user = "jessica"
lastName_user = "ribeiro"
email_user = "jessica@ribeiro.com"
password_user = "jessica12345"
phone_user = "981635518"
userStatus_user = 6652

url = "https://petstore.swagger.io/v2/user"
headers={'Content-Type': 'application/json'}


def test_post_user():
    user = open('./fixtures/json/user1.json')
    data = json.loads(user.read())


    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(data)
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['message'] == str(id_user)
    
    assert response_body['type'] == "unknown"

def test_get_user():

    response = requests.get(
        url=f'{url}/{username_user}',
        headers=headers
    )
    response_body = response.json()

    assert response.status_code == 200
    assert response_body['firstName'] == firstName_user
    assert response_body['email'] == email_user
    assert response_body['password'] == password_user

def test_put_user():

    user = open('./fixtures/json/userput.json')
    data = json.loads(user.read())

    response = requests.put(
        url=f'{url}/{username_user}',
        headers=headers,
        data=json.dumps(data)
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['message'] == str(id_user)
    assert response_body['type'] == 'unknown'

def test_delete_user():

    response = requests.delete(
        url=f'{url}/{username_user}',
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['message'] == username_user



@pytest.mark.parametrize('id,username,firstName,lastName,email,password,phone,userStatus', read_csv('./fixtures/csv/users.csv'))
def test_post_user_dinamico(id,username,firstName,lastName,email,password,phone,userStatus):
    user = {}
    user['id'] = int(id)
    user['username'] = username
    user['firstName'] = firstName
    user['lastName'] = lastName
    user['email'] = email
    user['password'] = password
    user['phone'] = phone
    user['userStatus'] = int(userStatus)

    response = requests.post(
        url=url,
        headers=headers,
        data=json.dumps(user)
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['message'] == str(user['id'])

@pytest.mark.parametrize('username', read_csv('./fixtures/csv/users.csv'))
def test_delete_user_dinamico(username):
    username = username[1]

    response = requests.delete(
        url=f'{url}/{username}',
        headers=headers
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['message'] == username

