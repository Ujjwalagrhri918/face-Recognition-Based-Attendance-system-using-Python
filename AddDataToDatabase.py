import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://faceattendancesystem-ccf9b-default-rtdb.firebaseio.com/"
})

ref = db.reference('Students')

data = {
    "002075" : {
        "name" : "Ujjwal Agrahari",
        "major": "CSE core",
        "starting_year":  2022,
        "last_attendance_time": "2023-09-18 12:00:00",
        "total_attendance" : 14,
        "standing" : "G",
        "year" : 2
         },
    "321654" : {
        "name" : "baiigan",
        "major": "CSE core",
        "starting_year":  2022,
        "last_attendance_time": "2023-09-18 12:00:00",
        "total_attendance" : 14,
        "standing" : "G",
        "year" : 2
    },
    "852741" : {
        "name" : "Ujjwal Agrahari",
        "major": "CSE core",
        "starting_year":  2022,
        "last_attendance_time": "2023-09-18 12:00:00",
        "total_attendance" : 14,
        "standing" : "G",
        "year" : 2
    },
    "963852" : {
        "name" : "Elon musk",
        "major": "CSE AI & ML",
        "starting_year":  2009,
        "last_attendance_time": "2022-01-18 10:26:57",
        "total_attendance" : 3,
        "standing" : "VG",
        "year" : 4
    }
}

for key, value in data.items():
    ref.child(key).set(value)