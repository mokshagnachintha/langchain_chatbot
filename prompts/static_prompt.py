from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
import streamlit as st
from langchain_core.prompts import PromptTemplate




load_dotenv()





chatmodel=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
result=chatmodel.invoke('what is the capital of india')
print(result.content)

st.title('research model')

paper_input=st.selectbox('select paper',['attention is all you need','bert','gpt-3','t5','transformers for natural language processing'])

style_input=st.selectbox('select style',['summarize','explain like im 5','key points','detailed analysis','critique'])

length_input=st.selectbox('select length',['short','medium','long'])

temp=PromptTemplate(
    input_variables=['paper','style','length'],
    template='give a {length} {style} of the research paper titled {paper}'
)
prompt = temp.invoke({
    'paper':paper_input,
    'style':style_input,
    'length':length_input
})




if st.button('summarize'):
    st.write('generating summary...')
    result=chatmodel.invoke(prompt) 
    st.write(result.content)                                       