from promt_bilder import PromptBuilder
import json

# Создание экземпляра класса PromptBuilder
builder1 = PromptBuilder()

# Создание файла критериев
prompt1 = builder1.create_prompt_file("criteria.json")
print(prompt1)

print("-------------------------------------")

with open('criteria.json', encoding='utf-8') as f:
    file_content = f.read()
    templates = json.loads(file_content)

# Создание второго экземпляра класса PromptBuilder
builder2 = PromptBuilder()

# Создание строки промпта из шаблонов
prompt2 = builder2.create_prompt_str(templates)
print(builder2.do_structure(builder2.criteria))
print(prompt2)
