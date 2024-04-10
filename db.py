import json


class DataBase:
    def __init__(self, connect):
        self.connect = connect

    def execute_query_json(self, query):
        cursor = self.connect.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        json_data = json.loads(result[0][0])
        cursor.close()
        return json_data

    @staticmethod
    def formatting_to_json(json_data):
        result = {}
        for row in json_data:
            result[row["Code"]] = row["Promt"]

        return json.dumps(result, ensure_ascii=False)
