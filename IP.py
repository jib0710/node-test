import pyttsx3 

engine = pyttsx3.init()
engine.serProperty('rate', 150)

def speak(text):
    engine.say(text)
    engine.runAndWait()
    

text ="안녕하세요 챗 GPT로 만드는 파이썬 작품들 입니다."
speak(text)






