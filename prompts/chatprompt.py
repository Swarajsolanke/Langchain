from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
load_dotenv()


chat_template=ChatPromptTemplate([
    ('system','you are a helpful {domain} assistant'),
    ('human','Explain in simple terms , what is {topic}'})
])

prompt=chat_template.invoke({"domain":"cricket","topic":"olympic"})
print(prompt)