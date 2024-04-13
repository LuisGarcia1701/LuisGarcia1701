import configuration
import requests
import data

def get_docs():
    return requests.get(configuration.URL_SERVICE + configuration.DOC_PATH)

def get_logs():
    return requests.get(configuration.URL_SERVICE + configuration.LOG_MAIN_PATH, params={"count":20})

def get_users_table():
    return requests.get(configuration.URL_SERVICE + configuration.USERS_TABLE_PATH)

response = get_docs()
logs = get_logs()
user_table = get_users_table()

print(response.status_code)
print(response.ok)
print(response.raw)
print("-------------------------------")
print(logs.status_code)
print(logs.headers)
print("-------------------------------")
print(user_table.status_code)
print(user_table.headers)
print("-------------------------------")

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # inserta la dirección URL completa
                         json=body,  # inserta el cuerpo de solicitud
                         headers=data.headers)  # inserta los encabezados

new_user = post_new_user(data.user_body)
print(new_user.status_code)
print(new_user.json())

def post_products_kits(products_id):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH, json=products_id, headers=data.headers)

product_kits= post_products_kits(data.product_ids);
print(product_kits.status_code)
print(product_kits.json())