# CAN Training - LLMs

```
python -m venv venv
source venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
ollama serve
ollama pull llama3
ollama run llama3
ollama pull deepseek-r1
ollama run deepseek-r1
python test.py
python test-with-streaming.py
python generate.py "How to write a machine learning system to predict meningitis?"
python generate.py "How to write a machine learning system to predict meningitis?" --model deepseek-r1
```