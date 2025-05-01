import ollama

response = ollama.chat(
    model='llama3', 
    messages=[{'role': 'user', 'content': 'How to write a machine learning system to predict meningitis?'}],
    stream=True
)

for chunk in response:
    print(chunk['message']['content'], end='', flush=True)
