# CAN Training - LLMs

You will need:
1. Install `ollama` from ollama.com.
2. Python 3+
3. Several gigabytes of disk space on your local machine

```
python -m venv venv
source venv/bin/activate

pip install --upgrade pip
pip install -r requirements.txt

ollama serve &

ollama pull llama3
ollama run llama3

ollama pull deepseek-r1
ollama run deepseek-r1

python test.py
python test-with-streaming.py
python generate.py "How to write a machine learning system to predict meningitis?"
python generate.py "How to write a machine learning system to predict meningitis?" --model deepseek-r1

streamlit run streamlit-test.py
streamlit run streamlit.py
```