import cv2
import pyrebase
import numpy as np
from keras.models import load_model

# Firebase configuration
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

# Set your Firebase paths
on_path = "/ImageON"
off_path = "/ImageOFF"

# Load the Keras model
model = load_model(r"C:\Users\Jash Progs\workshop\converted_keras\keras_model.h5", compile=False)

# Load the labels
class_names = open(r"C:\Users\Jash Progs\workshop\converted_keras\labels.txt", "r").readlines()

# OpenCV video capture
cap = cv2.VideoCapture(0)

# Function to recognize hand gesture
def recognize_gesture(frame):
    # Replace this with your actual hand gesture recognition code
    # You may need to preprocess the frame and feed it to your model
    # For simplicity, let's assume a dummy result
    prediction = 1  # 1 for on, 0 for off
    return prediction

while True:
    ret, frame = cap.read()

    # Perform hand gesture recognition
    gesture_result = recognize_gesture(frame)

    # Update Firebase based on the hand gesture
    if gesture_result == 1:
        db.child(on_path).set("on")
    else:
        db.child(off_path).set("off")

    # Resize the raw image into (224-height, 224-width) pixels for Keras model
    keras_image = cv2.resize(frame, (224, 224), interpolation=cv2.INTER_AREA)

    # Make the image a numpy array and reshape it to the model's input shape
    keras_image = np.asarray(keras_image, dtype=np.float32).reshape(1, 224, 224, 3)

    # Normalize the image array
    keras_image = (keras_image / 127.5) - 1

    # Predicts the model
    prediction = model.predict(keras_image)
    index = np.argmax(prediction)
    class_name = class_names[index]
    confidence_score = prediction[0][index]

    # Print prediction and confidence score
    print("Class:", class_name[2:], end="")
    print("Confidence Score:", str(np.round(confidence_score * 100))[:-2], "%")

    # Display the frame with recognized hand gesture
    cv2.imshow("Combined Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close the OpenCV windows
cap.release()
cv2.destroyAllWindows()
