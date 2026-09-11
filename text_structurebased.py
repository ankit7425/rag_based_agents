from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from gtts import gTTS

loader = PyPDFLoader("IPL_Overview.pdf")
docs = loader.lazy_load()  #loading the document lazily to avoid loading the entire document into memory at once
splitter = RecursiveCharacterTextSplitter(
    chunk_size=15,
    chunk_overlap=0,
  
)

result = splitter.split_documents(docs)

print(result)
print(len(result))