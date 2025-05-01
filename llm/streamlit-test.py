import streamlit as st

st.title("If you see this, Streamlit is working!")
st.text("Hello")
input = st.text_input("Prompt")
submit = st.button("Generate")

if input and submit:
  st.text(input)

