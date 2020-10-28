import json
import logging

import allure
import requests

from src.api.response import AssertableResponse
from src.resources.data_params import json_users


class ApiService(object):

    def __init__(self):
        self._api_url = json_users['api']

    def _get(self, url, cookie):
        logging.info("Method: GET")
        return requests.get("{}{}".format(self._api_url, url),
                            headers={'content-type': 'application/json', "JSESSIONID=": cookie})

    def _post(self, url, body, cookie):
        logging.info("Method: POST")
        return requests.post("{}{}".format(self._api_url, url), data=json.dumps(body),
                            headers={'content-type': 'application/json', "JSESSIONID=": cookie})

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

    def body_auth(self, user):
        username = json_users['creds'][user]['username']
        password = json_users['creds'][user]['password']
        body = {"username": username, "password": password}
        return username, password, body

    def auth(self, user):
        username, password, body = self.body_auth(user)
        logging.info(f"Login to *{self._api_url}/rest/auth/1/session/* with creds: username: {username} , password: {password}")
        response = requests.post(self ._api_url + "/rest/auth/1/session/", data=json.dumps(body),
                                 headers={'content-type': 'application/json'})
        cookie = response.json()['session']['value']
        return cookie

    def login(self, user):
        username, password, body = self.body_auth(user)
        with allure.step(f"Login with creds username: {username} , password: {password}"):
            response = requests.post(self._api_url + "/rest/auth/1/session/", data=json.dumps(body), headers={'content-type': 'application/json'})
        return AssertableResponse(response)


class Issue(ApiService):

    def __init__(self):
        super().__init__()

    def create_issue(self, user, create_user_body):
        return AssertableResponse(self._post("/rest/api/2/issue/", create_user_body, user))

    def get_info_issue(self, user, id_issue):
        return AssertableResponse(self._get("/rest/api/2/issue/" + id_issue, user))