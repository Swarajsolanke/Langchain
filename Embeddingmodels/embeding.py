from langchain_openai import OpenAIEmbeding
from dotenv import load_dotenv
load_dotenv()


embeding=OpenAIEmbeding(model="text-embedding-3-large",dimensions=32)

document=["delhi is the capital of india","kolkata is the capital of west bengal",
          "paris is the capital of france"]


result=embeding.embed_document(document)
print(str(result))



