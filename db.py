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
            return []

        query = """SELECT cl.Code, cl.Promt
            FROM CheckGroupLists cgl
            JOIN CheckLists cl ON cgl.CheckList = cl.id
            WHERE cgl.CheckGroup = {}
            """.format(check_group_value)

        cursor = self.connect.cursor()
        cursor.execute(query)
        result = cursor.fetchall()
        return result

    @staticmethod
    def formatting_to_json(data):
        string = "{\n"
        for i, row in enumerate(data):
            string += f'  "{row[0]}": "{row[1]}"'

            if i < len(data) - 1:
                string += ','
            string += '\n'

        string += "}"
        return string
