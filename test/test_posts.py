import random

import pytest

from src.api.api_services import PostsService
from src.api.conditions import status_code
from src.api.json_body import JSONBody
from src.resources.data_params import DataUI


class TestIssue():

    @pytest.fixture(autouse=True)
    def setup(self, faker):
        self.title = faker.word()
        self.title_2 = faker.word()
        self.body = faker.sentence()
        self.body_2 = faker.sentence()
        self.userId = random.randint(1, 101)

    def test_01(self):
        response = PostsService().create_one_post(JSONBody.create_post_json(self.title, self.body, self.userId))
        response.should_have(status_code(201))

