import logging

import allure


class AssertableResponse(object):

    def __init__(self, response):
        logging.info("Request \n url= {} \n body= {}".format(response.request.url, response.request.body))
        logging.info("Response \n status={} \n header={} \n body={}".format(response.status_code, response.headers, response.text))
        self._response = response

    def should_have(self, condition):
        logging.info("Assert: check condition: " + str(condition))
        condition.match(self._response)

    def parse_body(self, parsing):
        # logging.info("Extract value " + str(parsing))
        return parsing.extract(self._response)

