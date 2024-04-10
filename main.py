from promt_bilder import PromptBuilder
import pymssql
from db import DataBase

conn = pymssql.connect(
    host='80.73.9.240',
    user='gonchar',
    password='8c22T3xGpK',
    database='Calls'
)

database = DataBase(conn)

query = """SELECT cl.Code, cl.Promt
    FROM CheckGroupLists cgl
    JOIN CheckLists cl ON cgl.CheckList = cl.id
    WHERE cgl.CheckGroup = 3
    FOR JSON PATH;"""

rows = database.execute_query_json(query)

res = database.formatting_to_json(rows)


prompt = PromptBuilder().create_prompt_str(res)

print(prompt)

conn.close()
