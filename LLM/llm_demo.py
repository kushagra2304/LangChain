from langchain_openai import OpenAI
from dotenv import load_dotenv
load_dotenv()
llm=OpenAI(model_name="gpt-3.5-turbo",temperature=0.7)
res=llm.invoke("What is langchain?")
print(res)