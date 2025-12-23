from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from pathlib import Path
from langchain_core.prompts import load_prompt



load_dotenv()





chatmodel=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

print(result.content)

st.title('research model')

paper_input=st.selectbox('select paper',['attention is all you need','bert','gpt-3','t5','transformers for natural language processing'])

style_input=st.selectbox('select style',['summarize','explain like im 5','key points','detailed analysis','critique'])

length_input=st.selectbox('select length',['short','medium','long'])

temp = load_prompt('prompts/prompt_template.json')



if st.button('summarize'):
    chain= temp | chatmodel
    prompt=chain.invoke({'paper':paper_input,'style':style_input,'length':length_input})    

    st.write('generating summary...')
    st.write(prompt.content)