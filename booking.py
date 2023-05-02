import requests

import configuration
import data
import helper


def create_booking(body):
    return requests.post(url=configuration.URL + configuration.CREATE, json=body)


def delete_booking(id):
    headers = data.header_with_token.copy()
    headers["Cookie"] = 'token=' + get_token()
    return requests.delete(url=configuration.URL + configuration.DELETE + str(id), headers=headers)


def get_token():
    token = requests.post(url=configuration.URL + configuration.CREATE_TOKEN, json=data.user_body).json()["token"]
    return token
