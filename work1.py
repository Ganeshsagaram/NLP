import speech_recognition as sr

def work1():
    sp = sr.Recognizer()

    # Code for capturing audio using microphone or any other source

    with sr.Microphone() as source:
        print("Speak something...")
        audio = sp.listen(source)

    # Call recognize_google() on the Recognizer instance
    try:
        text = sp.recognize_google(audio)
        print("Recognized text:", text)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))

# Call the function
work1()
