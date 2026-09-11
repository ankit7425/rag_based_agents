import os
from dotenv import load_dotenv
load_dotenv()
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.3-70b-versatile",

    api_key=os.environ.get("GROQ_API_KEY")
)

query="tell me about the scope of AI engineer in future."

ans=llm.invoke(query)
print(ans.content)