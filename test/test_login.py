from src.api.api_services import Authorization
from src.resources.data_params import DataApi, DataUI


class TestExample():

    def test_positive_login(self):
        response = Authorization().auth(DataUI.MAIN_USER)
        print(response)

