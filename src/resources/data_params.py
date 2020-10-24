import logging

from os.path import dirname, abspath

from conftest import ROOT_DIR
from src.utils.utils import read_file

LOGGER = logging.getLogger(__name__)
configuration = read_file(ROOT_DIR + "//configuration.json")
input_data = read_file(ROOT_DIR + configuration["inputData"])
json_users = read_file(ROOT_DIR + configuration["dataJson"])
json_global_data = read_file(ROOT_DIR + configuration["global_data"])



class DataAPI:

    # def get_env(env_param):
    #     return env_param


    @staticmethod
    def email(user):
        login = json_users['environments'][env]['creds'][user]['email']
        return login

    @staticmethod
    def password(user):
        password = json_users['environments'][env]['creds'][user]['password']
        return password

    USER_DATA = input_data['user']
    USER_EMAIL = input_data['email_user']

    NON_EXIST_USER = json_global_data["non exist user"]