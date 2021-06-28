### Campbell Alexander
### Database development and Use
### Module 6

from pymongo import MongoClient

### MongoDB cluster access
url = "mongodb+srv://admin:<password>@cluster0.fk51n.mongodb.net/test"
client = MongoClient(url)
db = client.pytech
students = db.students
student_list = students.find({})


print("\n  -- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")

for doc in student_list:
    print("  Student ID: " + doc["student_id"] + "\n  First Name: " + doc["first_name"] + "\n  Last Name: " + doc["last_name"] + "\n")

result = students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Oakenshield II"}})

thorin = students.find_one({"student_id": "1007"})

print("\n  -- DISPLAYING STUDENT DOCUMENT 1007 --")


print("  Student ID: " + thorin["student_id"] + "\n  First Name: " + thorin["first_name"] + "\n  Last Name: " + thorin["last_name"] + "\n")

### End
input("\n\n  End of program, press any key to continue...")