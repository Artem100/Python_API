import json
import logging

import requests

from src.api.response import AssertableResponse
from src.resources.data_params import DataAPI, json_users


class ApiService(object):
    data_api = DataAPI()

    def __init__(self):
        self._api_url = json_users['environments']['API']
        self._auth_api_url = json_users['environments']['Auth API']

    def _get(self, url, cookie):
        logging.info("Method: GET")
        return requests.get("{}{}".format(self._api_url, url),
                            headers={'content-type': 'application/json', 'Authorization': cookie})

    def _post(self, url, body, cookie):
        logging.info("Method: POST")
        return requests.post("{}{}".format(self._api_url, url), data=json.dumps(body),
                            headers={'content-type': 'application/json', 'Authorization': cookie})

    def _post_form_data(self, url, form_data, cookie):
        logging.info("Method: POST")
        return requests.post("{}{}".format(self._api_url, url), data=form_data,
                            headers={'content-type': 'application/x-www-form-urlencoded', 'Authorization': cookie})

    def _put(self, url, body, cookie):
        logging.info("Method: PUT")
        return requests.put("{}{}".format(self._api_url, url), data=json.dumps(body),
                             headers={'content-type': 'application/json', 'Authorization': cookie})

    def _put_form_data(self, url, form_data, cookie, files=None):
        logging.info("Method: PUT")
        return requests.put("{}{}".format(self._api_url, url), data=form_data,  files=files,
                            headers={'content-type': 'application/x-www-form-urlencoded', 'Authorization': cookie})

    def _delete(self, url, cookie):
        logging.info("Method: DELETE")
        return requests.delete("{}{}".format(self._api_url, url),
                             headers={'content-type': 'application/json', 'Authorization': cookie})

    def auth(self, user):
        username = json_users['environments']['creds'][user]['username']
        password = json_users['environments']['creds'][user]['password']

        data = {"username": username, "password": password}

        logging.info("Login with creds: username:{} , password:{}".format(username, password))

        response = requests.post(self._auth_api_url + "/connect/token",
                                 headers={'content-type': 'application/x-www-form-urlencoded'}, data=data)
        cookie = response.json()["token_type"] + " " + response.json()["access_token"]
        return cookie

class ExampleApiClass(ApiService):

    def __init__(self):
        super().__init__()


    def example_api_method(self, user, create_user_body):
        cookie = self.auth(user)
        return AssertableResponse(self._post("/user/registerUser", create_user_body, cookie))