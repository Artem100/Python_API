import pytest

from src.api.api_services import Authorization, Issue
from src.api.conditions import status_code
from src.api.json_body import JSONBody
from src.resources.data_params import DataUI


class TestIssue():

    @pytest.fixture(scope='session')
    def setup(self):
        self.cookie = Authorization().auth(DataUI().MAIN_USER)
        return self.cookie

    # @pytest.fixture(scope='session')
    def test_create_issue(self, setup):
        project = "AQA220"
        summary = "Created issue used to API"
        type_issue_name = "Bug"
        id = "2e1cd1bb771978cda2c5e8f3f10539ab180613f6"
        cookie = setup

        response = Issue().create_issue(cookie, JSONBody().create_issue(project, summary, type_issue_name, id))
        # response = Issue().create_issue(cookie, JSONBody().create_issue(project, summary, type_issue_name))

    def test_get_issue(self, setup):
        cookie = setup
        response = Issue().get_info_issue(cookie, "EES-41")
        response.should_have(status_code(200))
