#recognises speech and stores it under a seperate child-class
import speech_recognition as sr
import pyrebase

config = {
  "apiKey": "AIzaSyBaPZYmfplZCCpii8TwJeklqkDyfyE3ooo",
  "authDomain": "idhan-project.firebaseapp.com",
  "databaseURL": "https://idhan-project-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "idhan-project",
  "storageBucket": "idhan-project.appspot.com",
  "messagingSenderId": "629087325250",
  "appId": "1:629087325250:web:3ccf19923cbf744a51f1db",
  "measurementId": "G-N2CSN355VP"
}

firebase = pyrebase.initialize_app(config)
db = firebase.database()

class FirebaseHandler:
    def __init__(self, base_class):
        self.base_class = base_class

    def set_value_in_firebase(self, recognised, input):
        # Set value under the specified child class within the base class
        db.child(self.base_class).child(recognised).set(input)
        print(f"Value '{input}' set under child class '{self.base_class}/{recognised}' in Firebase.")

def speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        text = recognizer.recognize_google(audio)
        print("You said:", text)
        return text
    except sr.UnknownValueError:
        print("Speech Recognition could not understand audio.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    # Replace these values with your own Firebase child class and base class
    firebase_base_class = "VoiceRecognition"
    firebase_child_class = "recognised"

    # Initialize FirebaseHandler with the base class

    
    firebase_handler = FirebaseHandler(firebase_base_class)

    # Get speech input
    speech_text = speech_to_text()

    # Set the obtained text in the Firebase child class within the base class
    if speech_text:
        firebase_handler.set_value_in_firebase(firebase_child_class, speech_text)
