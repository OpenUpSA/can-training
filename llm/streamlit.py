import streamlit as st
import requests
import json
import pandas as pd
from collections import Counter
import re

st.title("🦙 Ollama Local Chat")

model = st.text_input("Model name:", value="llama3")
system_prompt = st.text_area("System prompt", value="You are a helpful assistant.", height=100)
user_prompt = st.text_area("User prompt", height=150)
submit = st.button("Generate")

if submit and user_prompt.strip():
    with st.spinner("Generating response..."):
        try:
            response = requests.post(
                "http://localhost:11434/api/generate",
                json={
                    "model": model,
                    "prompt": user_prompt,
                    "system": system_prompt,
                    "stream": True
                },
                stream=True
            )

            if response.status_code == 200:
                full_response = ""
                placeholder = st.empty()
                for line in response.iter_lines(decode_unicode=True):
                    if line.strip():
                        try:
                            data = json.loads(line)
                            token = data.get("response", "")
                            full_response += token
                            placeholder.markdown(full_response)
                        except Exception as e:
                            st.error(f"Error parsing stream chunk: {e}")
                            break

                words = re.findall(r'\b\w+\b', full_response.lower())
                word_counts = Counter(words)
                most_common = word_counts.most_common(10)

                if most_common:
                    df = pd.DataFrame(most_common, columns=["Word", "Frequency"])
                    st.subheader("🔢 Top 10 Words in Response")
                    st.bar_chart(df.set_index("Word"))
                else:
                    st.info("No words found for chart.")

            else:
                st.error(f"Error {response.status_code}: {response.text}")

        except Exception as e:
            st.error(f"Failed to connect to Ollama: {e}")
