# Приклад роботи програми:

## Вихід готового промпта в консолі з файлу `criteria.json`, та з бази даних:

```
Please analyze the given dialogues by carefully considering the criteria I will provide. It is essential to provide accurate and specific responses. Kindly ensure that you cover all the necessary details and do not overlook any important points. Here are the essential parameters to analyze:
theme - a short description of the dialog, for a quick understanding of what is being talked about
classification - which of the following categories the call falls into, based on its content, purpose or other characteristics - \nFinance: Calls related to financial matters, such as paying bills, clarifying payments, or other monetary transactions.\nService: Calls related to service requests, including resolving general questions or making service requests, such as equipment repair or maintenance.\nReconnect: Calls from subscribers wishing to reconnect services that have been suspended or disconnected.\nNew Connection: Calls from new subscribers wishing to connect to services.\nRepair: Calls related to requests for equipment repair or technical support.\nTemporary Disconnection: Calls in which subscribers request that services be temporarily suspended.\nDisconnect: Calls in which subscribers decide to permanently disconnect from services.\nOther: Calls that do not fall into any of the above categories.
tonality - a general mood or emotional state that is expressed in the way you speak. It can be positive, negative, or neutral.
dynamics - is a change in emotional state or mood during a conversation or interaction? e.g., positive->negative, negative->positive
greeting - whether the operator is greeted or not: yes/no
identification - whether the operator identified the subscriber by address, personal account, or otherwise : yes/no
resolved - whether the subscriber's problem was solved or a technician was called to help: yes/no
additional questions - whether the operator has clarified whether the subscriber has any additional questions: yes/no
reason for application - whether the operator clarified what the customer had a question or what he/she could help with
Give the answer in the format of JSON, with a layered structure: 
{
  "theme": "",
  "classification": "",
  "tonality": "",
  "dynamics": "",
  "greeting": "",
  "identification": "",
  "resolved": "",
  "additional questions": "",
  "reason for application": ""
}
Give the answers in English.
```

