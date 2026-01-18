import speech_recognition as sr
import pyttsx3

r=sr.Recognizer()
def record_text():
    while(1):
            try:
                with sr.Microphone() as source:
                    r.adjust_for_ambient_noise(source, duration=0.2)
                    print("Speak Anything :")
                    audio = r.listen(source)
                    text = r.recognize_google(audio)
                    print("You said : {}".format(text))
                return text
            
            except sr.RequestError as e:
                print("Could not request results; {0}".format(e))

            except sr.UnknownValueError:
                print("unknown error occured")
    return

def output_text(text):
    f=open("output.txt","a")
    f.write(text+"\n")
    f.close()
    return

while(1):
    text =record_text()
    output_text(text)

    print("wrote text")