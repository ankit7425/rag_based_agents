from langchain_community.retrievers import WikipediaRetriever

retriever = WikipediaRetriever(k=2, language="en")
query = "the geopolitical history of India and Pakistan from the perspective of Chinese"
docs = retriever.invoke(query)

for i, doc in enumerate(docs):
    print(f"Document {i+1}:")
    print(f"Title: {doc.metadata.get('title')}")
    print(f"URL: {doc.metadata.get('url')}")
    print(f"Content: {doc.page_content[:500]}...\n")
