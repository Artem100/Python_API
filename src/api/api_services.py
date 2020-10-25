import json
import logging

import requests

from src.api.response import AssertableResponse
from src.resources.data_params import json_users


class ApiService(object):

    def __init__(self):
        self._api_url = json_users['api']

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

class Authorization(ApiService):

    def __init__(self):
        super().__init__()

    def auth(self, user):

        username = json_users['creds'][user]['username']
        password = json_users['creds'][user]['password']

        body = {"username": username, "password": password}

        logging.info(f"Login to *{self._api_url}/rest/auth/1/session/* with creds: username: {username} , password: {password}")

        response = requests.post(self._api_url + "/rest/auth/1/session/", data=json.dumps(body),
                                 headers={'content-type': 'application/json'})
        # cookie = response.json()["token_type"] + " " + response.json()["access_token"]
        # response.status_code("200")
        r = response.json()['session']['value']
        return r

class ExampleApiClass(ApiService):

    def __init__(self):
        super().__init__()


    def example_api_method(self, user, create_user_body):
        cookie = self.auth(user)
        return AssertableResponse(self._post("/user/registerUser", create_user_body, cookie))