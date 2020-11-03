class JSONBody:

    @staticmethod
    def login_json(value1, value2):
        json = {
            "key1": value1,
            "key2": value2
        }

        return json

    @staticmethod
    def post_body(title, body, userId):
        json = {
              "title": title,
              "body": body,
              "userId": userId
            }
        return json