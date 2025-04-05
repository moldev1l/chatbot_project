import speech_recognition as sr

for index, name in enumerate(sr.Microphone.list_microphone_names()):
    print(index, name)

r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print("Скажите что нибудь")
    audio = r.listen(source)
    query = r.recognize_(audio, language="ru-RU")
    print(query.lower())