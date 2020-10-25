from conftest import ROOT_DIR
from src.utils.ui_utils import read_file

configuration = read_file(ROOT_DIR + "//configuration.json")
input_data = read_file(ROOT_DIR + configuration["inputData"])
json_users = read_file(ROOT_DIR + configuration["dataJson"])
json_global_data = read_file(ROOT_DIR + configuration["global_data"])
image_folder_files = ROOT_DIR + "//src//resources//images_files//"
docs_files_folder = ROOT_DIR + "//src//resources//docs_files//"
log_files = ROOT_DIR + "//src//docs//logs//"
pdf_folder_files = ROOT_DIR + "//src//resources//other_files//pdf_files//"


class DataUI:

    MAIN_PAGE_UI_URL = ""

    @staticmethod
    def email(user):
        login = json_users['creds'][user]['email']
        return login

    @staticmethod
    def password(user):
        password = json_users['creds'][user]['password']
        return password

    USER_DATA = input_data['user']
    USER_EMAIL = input_data['email_user']
    TXT_FILE = docs_files_folder + "test.txt"

    NON_EXIST_USER = json_global_data["non exist user"]

    # PDF NAMES
    pdf_file_name = "Some_pdf.pdf"
    pdf_file = pdf_folder_files + pdf_file_name

class DataApi():

    MAIN_PAGE_API_URL = json_users['api']
