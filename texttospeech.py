from gtts import gTTS

text="Hello, I am Ankit. I am learning Python programming language. I am a beginner in Python. I want to learn Python programming language from scratch. I want to become a Python developer in future."
tts=gTTS(text=text,lang='en')
tts.save("hello.mp3")
print("Audio file has been created successfully.")