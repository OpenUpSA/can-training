import ollama

response = ollama.chat(model='llama3', messages=[
    {'role': 'user', 'content': 'How to write a machine learning system to predict meningitis?'}
])

print(response['message']['content'])
