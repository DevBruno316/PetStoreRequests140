# bibliotecas
import pytest # engine/framework de teste de unidade
import requests #framework de teste de API
import json
# 2- classe (opcional)

# 2.1 - atributos ou variáveis
pet_id = 420665201 # Código do animal
pet_name = "Tibor"
pet_category_id = 1
pet_category_name = "dog"
pet_tag_id = 1
pet_tag_name = "vacinado"
pet_status = "available"

#Informações em comum
url="https://petstore.swagger.io/v2/pet"
headers={'Content-Type': 'application/json'}
# 2.2- Funções / métodos

def test_post_pet():
    #Arrange
    #Dados de entrada estão no arquivo json
    pet = open('./fixtures/json/pet1.json')
    data = json.loads(pet.read())

    #Act
    response = requests.post(
       url=url,
       headers=headers,
       data=json.dumps(data), 
       timeout=5,
    )

    #Assert

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == pet_name
    assert response_body['category']['name'] == pet_category_name
    assert response_body['tags'][0]['name'] == pet_tag_name



def test_get_pet():
    #dados de entrada e saída/ resultado esperado estão na seção de atributos antes das funções
    response = requests.get(
        url=f'{url}/{pet_id}',
        headers=headers,
        #Não tem body
        timeout= 5
    ) 

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['name'] == pet_name
    assert response_body['category']['id'] == pet_category_id
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == pet_status

def test_put_pet():
    pet = open('./fixtures/json/pet2.json')
    data = json.loads(pet.read())

    response = requests.put(
        url=url,
        headers=headers,
        data=json.dumps(data),
        timeout=5
    )

    response_body = response.json()

    assert response.status_code == 200
    assert response_body['id'] == pet_id
    assert response_body['name'] == "Hannah"
    assert response_body['category']['name'] == "cat"
    assert response_body['category']['id'] == 2
    assert response_body['tags'][0]['name'] == pet_tag_name
    assert response_body['tags'][0]['id'] == pet_tag_id
    assert response_body['status'] == "sold"

def test_delete_pet():
    response = requests.delete(
        url=f'{url}/{pet_id}',
        headers=headers,
        timeout=5
    )

    response_body = response.json()
    assert response.status_code == 200
    assert response_body['code'] == 200
    assert response_body['message'] == f'{pet_id}'

