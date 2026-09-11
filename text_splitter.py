from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("IPL_Overview.pdf")
docs = loader.lazy_load()

splitter = CharacterTextSplitter(
    chunk_size=15,
    chunk_overlap=0,
    separator=''
)

result = splitter.split_documents(docs)

print(result)