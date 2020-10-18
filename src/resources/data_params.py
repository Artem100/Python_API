import logging

from sys import platform
from os.path import dirname, abspath
from os import getenv

from src.utils.utils import read_file

LOGGER = logging.getLogger(__name__)
ROOT_DIR = dirname(abspath(__file__))
configuration = read_file(ROOT_DIR + "//configuration.json")
input_data = read_file(ROOT_DIR + configuration["inputData"])
json_users = read_file(ROOT_DIR + configuration["dataJson"])
json_global_data = read_file(ROOT_DIR + configuration["global_data"])

class DataAPI:

    MAIN_PAGE_UI_URL = json_users['environments']['ui']

    @staticmethod
    def email(user):
        login = json_users['environments']['creds'][user]['email']
        return login

    @staticmethod
    def password(user):
        password = json_users['environments']['creds'][user]['password']
        return password

    USER_DATA = input_data['user']
    USER_EMAIL = input_data['email_user']

    NON_EXIST_USER = json_global_data["non exist user"]
    MAIN_ADMIN_ID = json_global_data['main_admin_id']