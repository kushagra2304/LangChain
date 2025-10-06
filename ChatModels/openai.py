from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
load_dotenv()
llm = ChatOpenAI(model_name="gpt-3.5-turbo",temperature=0.7,max_completion_tokens=500)
res=llm.invoke("What is llm?")
print(res)
# print(res.content)