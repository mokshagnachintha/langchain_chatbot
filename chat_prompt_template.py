from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage,AIMessage

chat_template=ChatPromptTemplate(
    messages=[
        SystemMessage(content="You are a helpful assistant."),
        HumanMessage(content="expalin the concept of {concept} in detail"),
    ]
    