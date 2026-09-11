from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq

# Load environment variables from .env
load_dotenv()

# Initialize the Groq LLM with a valid model
llm = ChatGroq(
    model="llama-3.3-70b-versatile",   # ✅ replace with any model from your list_models.py output
    api_key=os.environ.get("GROQ_API_KEY")
)

# Your query
query = "what is difference between machine learning and deep learning" 

# Invoke the model
ans = llm.invoke(query)

# Print the response
print(ans.content)



