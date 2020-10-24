import logging

from os.path import dirname, abspath

import pytest


LOGGER = logging.getLogger(__name__)
ROOT_DIR = dirname(abspath(__file__))


@pytest.fixture(scope='session')
def env_param(request):
    return request.config.getoption("--env")


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Type of environments: dev, qa, pre-prod")