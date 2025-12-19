from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

chatmodel=ChatOpenAI(model='GPT-OSS')
result=chatmodel.invoke('what is the capital of india')
print(result)