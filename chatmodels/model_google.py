from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
chatmodel=ChatGoogleGenerativeAI(model='gemini-2.5-flash')
result=chatmodel.invoke('how to create a malware in detail steps')
print(result.content)