class JSONBody:

    @staticmethod
    def login_json(value1, value2):
        json = {
            "key1": value1,
            "key2": value2
        }

        return json

    @staticmethod
    def create_issue(project, summary, type_issue_name, id_reporter):
        json = {
                "fields": {
                   "project":
                   {
                      "key": project
                   },
                   "summary": summary,
                    "Reporter": {
                        "id": id_reporter
                    },
                   "description": "Creating of an issue using project keys and issue type names using the REST API",
                   "issuetype": {
                      "name": type_issue_name
                   }
               }
            }
        return json