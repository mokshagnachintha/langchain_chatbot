from langchain.messages import SystemMessage, HumanMessage, AIMessage

from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv      

load_dotenv()   

chatmodel=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

m=[
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Hello, who won the world series in 2020?"),
]



result=chatmodel.invoke(m)


m=append(AIMessage(content=result.content)
         )
print(result.content)
