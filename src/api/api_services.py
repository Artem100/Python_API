import json
import logging
import requests

import allure

from src.api.response import AssertableResponse
from src.resources.data_params import json_users


class ApiService(object):

    def __init__(self):
        self._api_url = json_users['api']

    def _get(self, url):
        logging.info("Method: GET")
        return requests.get("{}{}".format(self._api_url, url),
                            headers={'content-type': 'application/json'})

    def _post(self, url, body):
        logging.info("Method: POST")
        return requests.post("{}{}".format(self._api_url, url), data=json.dumps(body),
                            headers={'content-type': 'application/json'})

    def _put(self, url, body):
        logging.info("Method: PUT")
        return requests.put("{}{}".format(self._api_url, url), data=json.dumps(body),
                             headers={'content-type': 'application/json'})

    def _delete(self, url):
        logging.info("Method: DELETE")
        return requests.delete("{}{}".format(self._api_url, url),
                             headers={'content-type': 'application/json'})

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


class PostsService(ApiService):

    def __init__(self):
        super().__init__()

    url = "/posts/"

    def create_one_post(self, body):
        return AssertableResponse(self._post(self.url, body))

    def get_info_about_post(self, id_post):
        return AssertableResponse(self._get(self.url+id_post))

    def update_post(self, id_post, body):
        return AssertableResponse(self._put(self.url+id_post, body))

    def delete_post(self, id_post):
        return AssertableResponse(self._delete(self.url+id_post))


# class WithCookie(ApiService):
#
#     def __init__(self):
#         super().__init__()
#
#     def create_issue(self, user, create_user_body):
#         return AssertableResponse(self._post("/posts", create_user_body, user))
#
#     def get_info_issue(self, user, id_issue):
#         return AssertableResponse(self._get("/rest/api/2/issue/" + id_issue, user))