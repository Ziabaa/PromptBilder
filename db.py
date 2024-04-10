import json


class DataBase:
    def __init__(self, connect):
        self.connect = connect

    def execute_query_json(self, param):

        if param == "calls":
            check_group_value = 4
        elif param == "chats":
            check_group_value = 3
        else:
            return None

        query = """SELECT cl.Code, cl.Promt
            FROM CheckGroupLists cgl
            JOIN CheckLists cl ON cgl.CheckList = cl.id
            WHERE cgl.CheckGroup = {}
            FOR JSON PATH;""".format(check_group_value)

        cursor = self.connect.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        json_data = json.loads(result[0][0])
        cursor.close()
        res = DataBase.formatting_to_json(json_data)
        return res

    @staticmethod
    def formatting_to_json(json_data):
        result = {}
        for row in json_data:
            result[row["Code"]] = row["Promt"]

        return json.dumps(result, ensure_ascii=False)
