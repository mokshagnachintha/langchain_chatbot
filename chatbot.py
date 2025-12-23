from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from langchain.messages import SystemMessage,HumanMessage,AIMessage

load_dotenv()

chatmodel=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
chat_history=[]
chat_history.append(SystemMessage(content='you are a helpful assistant.'))
while True:
    user_input=input("you: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input=='exit':
        break
    result=chatmodel.invoke(chat_history)
    chat_history.append(AIMessage(content=result.content))  
    print("bot:",result.content)
    
print(chat_history)
    