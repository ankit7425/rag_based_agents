from langchain_community.document_loaders import PyPDFLoader
loader=PyPDFLoader("IPL_Overview.pdf")
docs=loader.load()
print(docs)
