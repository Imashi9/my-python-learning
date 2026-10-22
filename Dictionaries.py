student = {"name": "John", "age": 25, "courses": ["Math", "CompSci"]}
print(student)
print(student["name"]) #This willprint the value of the key "name" in the dictionary student
print(student.get("name")) #This will print the value of the key "name" in the dictionary student
print(student.get("phone", "Not Found")) #This will print the value of the key "phone" in the dictionary student, if the key does not exist it will print "Not Found"