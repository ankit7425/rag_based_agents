from langchain_community.retrievers import WikipediaRetriever


retriever = WikipediaRetriever(k=2,language="en")
query = "the geopolitical history of india and pakistan from the prospective of chienese"

docs = retriever.invoke(query)

for i ,doc in enumerate(docs):
    print(f"Document {i+1}:")
    print(f"Title: {doc.metadata.get('title')}")
    print(f"URL: {doc.metadata.get('url')}")
    print(f"Content: {doc.page_content[:500]}...\n")  # Print first 500 characters
  
    


   # didn't work because of the following error:
#Traceback (most recent call last):  