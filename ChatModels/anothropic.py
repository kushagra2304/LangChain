from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
load_dotenv()
llm = ChatAnthropic(model_name="claude-2",temperature=0.7,max_completion_tokens=500)
res=llm.invoke("What is llm?")  
print(res)