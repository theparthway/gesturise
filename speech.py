import random
import time

import speech_recognition as sr
# import appcopys


# def recognize_speech_from_mic(recognizer, microphone):
#     if not isinstance(recognizer, sr.Recognizer):
#         raise TypeError("`recognizer` must be `Recognizer` instance")

#     if not isinstance(microphone, sr.Microphone):
#         raise TypeError("`microphone` must be `Microphone` instance")

#     with microphone as source:
#         recognizer.adjust_for_ambient_noise(source)
#         audio = recognizer.listen(source)

#     response = {
#         "success": True,
#         "error": None,
#         "transcription": None
#     }

#     try:
#         response["transcription"] = recognizer.recognize_google(audio)
#     except sr.RequestError:
#         response["success"] = False
#         response["error"] = "API unavailable"
#     except sr.UnknownValueError:
#         response["error"] = "Unable to recognize speech"

#     return response

# def start():
#     recognizer = sr.Recognizer()
#     microphone = sr.Microphone()

#     for i in range(5):
#         # for j in range(5):
#         print('Speak!')
#         guess = recognize_speech_from_mic(recognizer, microphone)
#         print("I didn't catch that. What did you say?\n")

#         if guess["error"]:
#             print("ERROR: {}".format(guess["error"]))

#         # show the user the transcription
#         print("You said: {}".format(guess["transcription"]))
#         if (guess["transcription"] == "gesture"):
#             appcopy.gesture()

def start():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 1
        r.adjust_for_ambient_noise(source)
        print("Listening...")
        audio = r.listen(source)
    try:
        print("Recognizing...")
        query= r.recognize_google(audio,language= 'en-in')
        print(f"user said: {query}\n")
    except Exception as e:
        print("Couldn't recognize what you said, speak once more.")
        return None
    return query