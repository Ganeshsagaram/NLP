import speech_recognition as sr

def show_speech_recognition_functions():
    print("Available methods and functions in SpeechRecognition library:\n")

    # Get all attributes of the SpeechRecognition module
    speech_recognition_attrs = dir(sr)

    # Filter and display only functions and methods
    for attr in speech_recognition_attrs:
        if callable(getattr(sr, attr)):
            print(attr)

# Call the function to display available functions and methods in SpeechRecognition
show_speech_recognition_functions()
