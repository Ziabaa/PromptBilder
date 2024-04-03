import json
import tiktoken


class PromptBuilder:
    criteria = []
    param_prompt = []

    @staticmethod
    def get_data_json(file):
        with open(file, encoding='utf-8') as f:
            file_content = f.read()
            templates = json.loads(file_content)

        return templates

    @staticmethod
    def token_counter(string):
        encoding = tiktoken.get_encoding("cl100k_base")
        num_tokens = len(encoding.encode(string))
        return num_tokens

    @classmethod
    def write_data(cls, data):
        for key, value in data.items():
            if not key or not value:
                print("At least one parameter is empty!")
            else:
                cls.criteria.append(key)
                cls.param_prompt.append(value)

    @classmethod
    def do_prompt(cls):
        string = ""
        for prompt, key in zip(cls.param_prompt, cls.criteria):
            string += key + " - " + prompt + '\n'
        return string

    @classmethod
    def do_structure(cls):
        string = "{\n"
        for i, key in enumerate(cls.criteria):
            string += "  \"" + key + "\": " + "\"\""
            if i != len(cls.criteria) - 1:
                string += ","
            string += '\n'

        string += "}"
        return string

    @staticmethod
    def connect_final_prompt(param_prompt, structure_prompt):
        start_prompt = ("Please analyze the given dialogues by carefully considering the criteria I will provide. It "
                        "is essential to provide accurate and specific responses. Kindly ensure that you cover all "
                        "the necessary details and do not overlook any important points. Here are the essential "
                        "parameters to analyze:\n")

        final_prompt = start_prompt + param_prompt
        json_structure_prompt = "Give the answer in the format of JSON, with a layered structure: \n"
        final_prompt += json_structure_prompt + structure_prompt
        return final_prompt

    @classmethod
    def create_prompt(cls, file):
        prompt = cls

        data = prompt.get_data_json(file)
        prompt.write_data(data)

        param = prompt.do_prompt()
        struct = prompt.do_structure()

        return prompt.connect_final_prompt(param, struct)
