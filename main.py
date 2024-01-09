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
};

firebase = pyrebase.initialize_app(config)

db = firebase.database()
while True:
    x= db.child("led").child("led status").set("2")
    x= db.child("led").child("led status").get().val()
    print(x)

    y=db.child("fan").child("fan status").set("on")
    y=db.child("fan").child("fan status").get().val()
    print(y)

    z=db.child("light").child("light status").set("off")
    z=db.child("light").child("light status").get().val()
    print(z)