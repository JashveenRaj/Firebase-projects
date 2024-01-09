#Code to control fan,light and led based on speech recognition

import speech_recognition as sr
import pyrebase

# Firebase has been initialized 

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

# Initialize the speech recognition
recognizer = sr.Recognizer()

#listen and update light status

def listen_and_update_light_status():
    with sr.Microphone() as source:
        print("Say 'light on' or 'light off' to control the light:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said: " + command)

        if "light on" in command:
            light_status = "on"
        elif "light off" in command:
            light_status = "off"
        else:
            print("Invalid command. Please say 'light on' or 'light off'.")
            return

        # Update the light status in the Firebase database
        db.child("light").child("light status").set(light_status)
        print(f"Light status set to {light_status}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

#Listen and update fan status

def listen_and_update_fan_status():
    with sr.Microphone() as source:
        print("Say 'fan on' or 'fan off' to control the led:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said: " + command)

        if "fan on" in command:
            fan_status = "on"
        elif "fan off" in command:
            fan_status = "off"
        else:
            print("Invalid command. Please say 'fan on' or 'fan off'.")
            return

        # Update the light status in the Firebase database
        db.child("fan").child("fan status").set(fan_status)
        print(f"fan status set to {fan_status}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

#Listen and update led status

def listen_and_update_led_status():
    with sr.Microphone() as source:
        print("Say 'led on' or 'led off' to control the led:")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source, timeout=5)

    try:
        command = recognizer.recognize_google(audio).lower()
        print("You said: " + command)

        if "led on" in command:
            led_status = "on"
        elif "led off" in command:
            led_status = "off"
        else:
            print("Invalid command. Please say 'led on' or 'led off'.")
            return

        # Update the light status in the Firebase database
        db.child("led").child("led status").set(led_status)
        print(f"led status set to {led_status}")

    except sr.UnknownValueError:
        print("Sorry, I could not understand your command.")
    except sr.RequestError as e:
        print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    while True:

        #listen and update led status
        listen_and_update_led_status()

        # Use the existing code to get and print the status of LED and fan
        x = db.child("led").child("led status").get().val()
        print("LED Status:", x)

        #listen and update fan status
        listen_and_update_fan_status()

        y = db.child("fan").child("fan status").get().val()
        print("Fan Status:", y)

        # Listen for voice command and update the light status
        listen_and_update_light_status()

        # Print the updated light status
        z = db.child("light").child("light status").get().val()
        print("Light Status:", z)
