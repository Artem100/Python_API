import logging

from sys import platform
from os.path import dirname, abspath



LOGGER = logging.getLogger(__name__)
ROOT_DIR = dirname(abspath(__file__))
DOWNLOAD_DIR = ROOT_DIR + "//download_files"


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default="qa", help="Type of browser: dev, qa, pre-prod")



