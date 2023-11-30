# speech_to_text/speech_recognition_module.py
import speech_recognition as sr

def recognize_realtime_speech():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")

        while True:
            try:
                recognizer.adjust_for_ambient_noise(source)
                audio_data = recognizer.listen(source, timeout=5)  # Set a timeout to avoid blocking indefinitely

                text = recognizer.recognize_google(audio_data)
                print("Recognized speech:", text)

                # Add a condition to break out of the loop if a specific word is detected
                if "stop" in text.lower():
                    print("Stopping speech recognition.")
                    break

            except sr.UnknownValueError:
                pass
            except sr.RequestError as e:
                print(f"Error with the speech recognition service; {e}")
