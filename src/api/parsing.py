import abc
import logging

class Parsing():

    def __init__(self):
        pass

    @abc.abstractmethod
    def extract(self, response):
        return

class ExtractField(Parsing):

    def __init__(self, field):
        super().__init__()
        self._field = field

    def extract(self, response):
        try:
            value = response.json()[self._field]
            return value
        except KeyError:
            assert False, "\nResponse body doesn't have *{}* field".format(self._field)

    def __repr__(self):
        return "in field: *{}*".format(self._field)

extract_field = ExtractField


class ExtractFieldListValue(Parsing):


    def __init__(self, field, index):
        super().__init__()
        self._field = field
        self._index = index

    def extract(self, response):
        try:
            logging.info(f"Extract values from key path: [{self._field}][{self._index}]")
            return response.json()[self._field][self._index]
        except KeyError:
            assert False, "\nResponse body doesn't have *{}* field".format(self._field)

extract_field_list_value = ExtractFieldListValue



class ExtractCompany(Parsing):

    '''
        field:{value1, value2}
    '''

    def __init__(self, field, index, index2, index3):
        super().__init__()
        self._field = field
        self._index = index
        self._index2 = index2
        self._index3 = index3

    def extract(self, response):
        try:
           return response.json()[self._field][self._index][self._index2][0][self._index3]
        except KeyError:
            assert False, "\nResponse body doesn't have *{}* field".format(self._field)

    def __repr__(self):
        return "value from list: *{}*".format(self._field)

extract_company =  ExtractCompany


class GetDealID(Parsing):

    def extract(self, response):
        try:
            return response.json()["data"]["dealIds"][0]
        except KeyError:
            assert False, "\nResponse body doesn't have *{}* field".format(response.json()["data"]["dealIds"])

get_id_deal = GetDealID


class GetCompanyID(Parsing):

    def extract(self, response):
        try:
            return response.json()["data"][0]
        except KeyError:
            assert False, "\nResponse body doesn't have *{}* field".format(response.json()["data"]["dealIds"])


get_id_company = GetCompanyID

class GetErrorLogin(Parsing):

    def extract(self, response):
        try:
            return response.json()["errorMessages"][0]
        except KeyError:
            assert False, f"\nResponse body doesn't have *{response.json()['errorMessages'][0]}* field"

get_error_login = GetErrorLogin





