import pyrebase
Config = {
  "apiKey": "AIzaSyA7ic2PWsIINSgU4AvtbAzR_YrlUo_DyIs",
  "authDomain": "vinoth-eef7e.firebaseapp.com",
  "databaseURL": "https://vinoth-eef7e-default-rtdb.asia-southeast1.firebasedatabase.app",
  "projectId": "vinoth-eef7e",
  "storageBucket": "vinoth-eef7e.appspot.com",
  "messagingSenderId": "279807573282",
  "appId": "1:279807573282:web:93a6ee9884355fab2c797b",
  "measurementId": "G-6FR0J9EX68"
};

firebase = pyrebase.initialize_app(Config)
db  = firebase.database()
while True:
    x = db.child("room").child(" motor status").set("on")
    y = db.child("room").child(" led status").set("on")
    z = db.child("room").child(" fan status").set("on")    
    print(x,y,z)
    # print(y)
    # print(z)