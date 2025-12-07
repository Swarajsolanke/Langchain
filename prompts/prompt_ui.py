from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate,load_prompt
from streamlit import st
load_dotenv()


model=ChatOpenAI()



st.header("Prompt Template Example")

paper_input=st.selectbox("select Reseach paper name",["Attension is all you need",
                                                      "BERT: Pre-training of Deep Bidirectional Transformers for Language Understanding",])

style_input=st.selectbox("select writing style",["Formal","Informal","Humorous","Sarcastic"])   

length_input=st.slider("Select the length of summary",50,300,100)   

template=load_prompt('template.json')


if st.button("Generate Summary"):
    chain=template|model
    result=chain.invoke({"paper_input":paper_input,
                  "style_input":style_input,        
                  "length_input":length_input})
    
    st.write(result.content)

    st.write(result.content)