import abc

class Conditions():

    def __init__(self):
        pass

    @abc.abstractmethod
    def match(self, response):
        return

class StatusCodeCondition(Conditions):

    def match(self, response):
        #try:
        assert response.status_code == self._status_code, "\nExpected status code: {} \nActual status code: {}".format(self._status_code, response.status_code)
        #except AssertionError:
            #assert False, "\nExpected status code: {} \nActual status code: {}".format(self._status_code, response.status_code)

    def __init__(self, code):
        super().__init__()
        self._status_code = code


    def __repr__(self):
        return "status code is {}".format(self._status_code)

status_code = StatusCodeCondition


class FieldAndValue(Conditions):

    '''
        For field format:
        {
            "name_field":"value"
        }
    '''

    def match(self, response):
        try:
            json = response.json()
            assert self._value == json[self._key]
        except KeyError:
            assert False, "\nResponse body doesn't have *{}* field".format(self._key)
        except:
            assert False, "*{0}* key hasn't value: '{1}' \nIt's has value: '{2}'".format(self._key, self._value, json[self._key])

    def __init__(self, key, value):
        super().__init__()
        self._key = key
        self._value = value

    def __repr__(self):
        return "Check value *{}* in key *{}*".format(self._value, self._key)

field_and_value = FieldAndValue


class ValueGreaterThan(Conditions):

    """
    value_of_field > count_number
    """

    def __init__(self, field, value):
        super().__init__()
        self._field = field
        self._value = value

    def match(self, response):
        try:
            json = response.json()
            field = len(str(json[self._field]))
            value_length = int(self._value)
            assert field > value_length
        except AssertionError:
            assert False, "\nField *{}* hasn't a length of value more than *{}*, it has: *{}*".format(self._field, self._value, len(json[self._field]))
        except KeyError:
            assert False, "\nResponse body doesn't have *{}* field".format(self._field)

    def __repr__(self):
        return "Field {} has a length of value more than *{}*".format(self._field, self._value)


value_greater_than = ValueGreaterThan




class OneIndexFieldValue(Conditions):

    '''
    For field format :
    {
        "root_field":
            {
                "name_field":"value"
            }
    }
    '''

    def match(self, response):
        try:
            json = response.json()
            assert self._value == json[self._root_key][self._field]
        except AssertionError:
            assert False, \
                "\nIndex *[{0}][{1}]* doesn't have value: '{2}'.\nIt's has value: '{3}'"\
                .format(self._root_key, self._field, self._value, json[self._root_key][self._field])
        except KeyError:
            assert False, "\nResponse body doesn't have index: [{}][{}]".format(self._root_key, self._field)

    def __init__(self, root_key, field, value):
        super().__init__()
        self._root_key = root_key
        self._field = field
        self._value = value

    def __repr__(self):
        return "Check value *{}* in key: {}{}".format(self._value, self._root_key, self._field)


one_index_field_value = OneIndexFieldValue