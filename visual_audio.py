import matplotlib.pyplot as plt
import numpy as np
import speech_recognition as sr

# Initialize the recognizer
recognizer = sr.Recognizer()

# Record audio from the microphone
with sr.Microphone() as source:
    print("Speak something...")
    audio = recognizer.listen(source,timeout=1)
    # print(audio)
# recognizer.operation_timeout(10)
# Convert speech to text
text = recognizer.recognize_google(audio)
print(text)
# Get the audio samples and sample rate
audio_data = np.frombuffer(audio.frame_data, np.int16)
sample_rate = audio.sample_rate

# Get the time axis for the waveform
duration = len(audio_data) / sample_rate
time = np.linspace(0, duration, len(audio_data))

# Plot the waveform
plt.figure(figsize=(10, 4))
plt.plot(time, audio_data)
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.title('Speech Voice Signal')
plt.grid(True)
plt.show()
