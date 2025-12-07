from langchain_openai import OpenAIEmbedding
from dotenv import load_dotenv


load_dotenv()
embedding_model=OpenAIEmbedding(model="text-embedding-ada-002",dimensions=32)

result=embedding_model.embed_query("delhi is the capital of india")

print(str(result))