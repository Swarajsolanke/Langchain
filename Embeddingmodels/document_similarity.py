from langchain_openai import OpenAIEmbedding
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
load_dotenv()

embedding_model=OpenAIEmbedding(model="text-embedding-ada-002",dimensions=32)   
documnts=["delhi is the capita of indian",
          "kolkata is the capital of west bengal",
          "paris is the capital of france",
          "gandhinagar is the capital of gujarat"]


query='tell me captial of india'


doc_embedding=embedding_model.embed_documents(documnts)
query_embedd=embedding_model.embed_query(query)

score=cosine_similarity([query_embedd],doc_embedding)[0]


index,score=sorted(list(enumerate(score)),key=lambda x:x[1])[-1]


print(query)
print(documnts[index])
print("similarity score:",score)
