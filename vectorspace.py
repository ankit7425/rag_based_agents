from langchain_ollama import OllamaEmbeddings
from langchain_core.vectorstores import InMemoryVectorStore
from langchain_core.documents import Document

# Create sample documents
doc1 = Document(
    page_content="Machine Learning is a branch of Artificial Intelligence.",
    metadata={"author": "Andrew Smith"}
)

doc2 = Document(
    page_content="Natural Language Processing (NLP) is a subfield of AI that focuses on language understanding.",
    metadata={"author": "Emily Johnson"}
)

# Create embeddings and store them
embeddings = OllamaEmbeddings(model="nomic-embed-text")
vectorstore = InMemoryVectorStore(embedding=embeddings)

# Add documents to the vectorstore
vectorstore.add_documents([doc1, doc2], ids=["id1", "id2"])

# Retrieve similar documents
query = "What is NLP?"
results = vectorstore.similarity_search(query, k=2)

for i, doc in enumerate(results):
    print(f"Document {i+1}:")
    print(f"Author: {doc.metadata.get('author')}")
    print(f"Content: {doc.page_content}\n")



