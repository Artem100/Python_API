from src.api.api_services import Authorization
from src.api.conditions import status_code
from src.api.parsing import extract_field, extract_field_list_value, get_error_login
from src.resources.data_params import DataApi, DataUI


class TestExample():

    def test_cookie_login(self):
        response = Authorization().auth(DataUI.MAIN_USER)
        print(response)

    def test_positive_login(self):
        response = Authorization().login(DataUI.MAIN_USER)
        response.should_have(status_code(200))
        assert response.parse_body(extract_field_list_value("session", "name")) == "JSESSIONID"
        assert len(response.parse_body(extract_field_list_value("session", "value"))) >= 1


    def test_invalid_username_password(self):
        response = Authorization().login(DataUI.INCORRECT_CREDS)
        response.should_have(status_code(401))
        assert response.parse_body(get_error_login) == "Login failed"


