import random

import pytest

from src.api.api_services import PostsService
from src.api.conditions import status_code, field_and_value
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
        self.userId_2 = random.randint(1, 101)
        self.post_id = "100"
        self.post_id_delete = "101"

    def test_01(self):
        response = PostsService().create_one_post(JSONBody.post_body(self.title, self.body, self.userId))
        response.should_have(status_code(201))

    def test_02(self):
        response = PostsService().get_info_about_post(self.post_id)
        response.should_have(status_code(200))
        response.should_have(field_and_value("id", 100))
        response.should_have(field_and_value("title", "at nam consequatur ea labore ea harum"))

    def test_03(self):
        response = PostsService().update_post(self.post_id, JSONBody.post_body(self.title_2, self.body_2, self.userId_2))
        response.should_have(status_code(200))
        response.should_have(field_and_value("title", self.title_2))
        response.should_have(field_and_value("body", self.body_2))
        response.should_have(field_and_value("userId",  self.userId_2))

    def test_04(self):
        response = PostsService().delete_post(self.post_id_delete)
        response.should_have(status_code(200))

    def test_05(self):
        response = PostsService().get_info_about_post(self.post_id_delete)
        response.should_have(status_code(404))
