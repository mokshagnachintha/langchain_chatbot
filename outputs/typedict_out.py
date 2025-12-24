from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
from typing import TypedDict


load_dotenv()

model=ChatGoogleGenerativeAI(model='gemini-2.5-flash')

class output(TypedDict):
    summary: str
    sentiment: str
    
    
structured_model=model.with_structured_output(output)


result=structured_model.invoke('the mobile is really good but the battery life is too short. the dispaly is also very nice.')

print(result)

