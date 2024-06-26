import json
import tiktoken


class PromptBuilder:
    def __init__(self):
        self.criteria = []
        self.param_prompt = []
        self.final_prompt = ""
        self.final_structure = ""

    @staticmethod
    def get_data_json_file(file):
        with open(file, encoding='utf-8') as f:
            file_content = f.read()
            templates = json.loads(file_content)

        return templates

    @staticmethod
    def get_data_json_string(json_string):
        templates = json.loads(json_string)
        return templates

    @staticmethod
    def token_counter(string):
        encoding = tiktoken.get_encoding("cl100k_base")
        num_tokens = len(encoding.encode(string))
        return num_tokens

    def write_data(self, data):
        self.criteria.clear()
        self.param_prompt.clear()
        for key, value in data.items():
            if not key or not value:
                print("At least one parameter is empty!")
            else:
                self.criteria.append(key)
                self.param_prompt.append(value)

    def do_prompt(self):
        string = ""
        for prompt, key in zip(self.param_prompt, self.criteria):
            string += key + " - " + prompt + '\n'
        return string

    @staticmethod
    def do_structure(criteria):
        string = "{\n"
        for i, key in enumerate(criteria):
            string += "  \"" + key + "\": " + "\"\""
            if i != len(criteria) - 1:
                string += ","
            string += '\n'

        string += "}"

        return string

    @staticmethod
    def connect_final_prompt(param_prompt, structure_prompt, language):
        if language == "en":
            lang = "English"
        elif language == "ru":
            lang = "Russian"
        else:
            lang = "Ukrainian"

        start_prompt = ("Please analyze the given dialogues by carefully considering the criteria I will provide. It "
                        "is essential to provide accurate and specific responses. Kindly ensure that you cover all "
                        "the necessary details and do not overlook any important points. Here are the essential "
                        "parameters to analyze:\n")

        final_prompt = start_prompt + param_prompt
        json_structure_prompt = "Give the answer in the format of JSON, with a layered structure: \n"
        final_prompt += json_structure_prompt + structure_prompt + f"\nGive the answers in {lang}."
        return final_prompt

    @staticmethod
    def create_prompt(data, lang, param: str = "string") -> str:  # Param is: String json or file json ... string/file
        build = PromptBuilder()

        # Проверка корректности параметра param
        if param not in {"string", "file"}:
            raise ValueError("Invalid data source. Please specify 'file' or 'string'.")

        # Обработка данных в зависимости от параметра param
        if param == "file":
            data = build.get_data_json_file(data)
        elif param == "string":
            data = build.get_data_json_string(data)

        # Создание промпта
        build.write_data(data)
        param = build.do_prompt()
        struct = build.do_structure(build.criteria)
        final_prompt = build.connect_final_prompt(param, struct, lang)

        return final_prompt
