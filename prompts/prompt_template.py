from langchain_core import HUmanMessage
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()


model=ChatOpenAI()


template2=PromptTemplate(
    template="greet this person . the name of persin is {name}",
    input_variables=["name"]
)

prompt=template2.invoke({"name":"alice"})

result=model.invoke(prompt)

print(result.content)


