from langchain_community.document_loaders import TextLoader
from gtts import gTTS

loader = TextLoader(r"C:\Users\goodb\OneDrive\Desktop\gen ai\rag\IPL_Overview.txt")
documents = loader.load()
tts=gTTS(text=documents[0].page_content, lang='en')
tts.save("ipl_overview.mp3")
print(documents)
print ("Audio file has been created successfully.")




