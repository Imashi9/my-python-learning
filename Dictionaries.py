student = {"name": "John", "age": 27, "courses": ["Math", "CompSci"]}
# print(student)
# print(student["name"]) #This willprint the value of the key "name" in the dictionary student
# print(student.get("name")) #This will print the value of the key "name" in the dictionary student
# print(student.get("phone", "Not Found")) #This will print the value of the key "phone" in the dictionary student, if the key does not exist it will print "Not Found"

# student["phone"] = "555-5555" #This will add the key "phone" with the value "555-5555" to the dictionary student
# print(student)

# student.update({"name": "Jane", "age": 26, "phone": "555-5555"}) #This will update the values of the keys "name" and "age" in the dictionary student and add the key "phone" with the value "555-5555"
# print(student)

# del student["age"] #This will delete the key "age" from the dictionary student
# print(student)

# age = student.pop("age") #This will remove the key "age" from the dictionary student and return its value
# print(age)

# print(student.keys()) #This will print all the keys in the dictionary student
# print(student.values()) #This will print all the values in the dictionary student   
# print(student.items()) #This will print all the key-value pairs in the dictionary student

for key in student:
    print(key) #This will print all the keys in the dictionary student  
for value in student.values():
    print(value) #This will print all the values in the dictionary student
for key, value in student.items():
    print(key, value) #This will print all the key-value pairs in the dictionary student