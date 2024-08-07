# -*- coding: utf-8 -*-
"""response_build.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1fmBtQup7mTDl_iR_E0xlPS3YaMFnCqe-
"""

pip install streamlit openai langchain-community langchain-core

import streamlit as st
import openai
from langchain.llms import OpenAI

st.title("Quick start App")

openai_api_key = st.sidebar.text_input("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")

def generate_response(input_text):
  llm = OpenAI(temperature=0.7, openai_api_key=openai_api_key)
  st.info(llm(input_text))

with st.form('my_form'):
  text = st.text_area('Enter text:', 'What are the three key pieces of advice for learning how to code?')
  submitted = st.form_submit_button('Submit')
  if not openai_api_key.startswith('sk-'):
    st.warning('Please enter your OpenAI API key!', icon='⚠')
  if submitted and openai_api_key.startswith('sk-'):
    generate_response(text)

