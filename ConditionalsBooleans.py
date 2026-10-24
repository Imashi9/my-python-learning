# language = "C++"

# if language == "Python":
#     print("Language is Python.")
# elif language == "Java":
#     print("Language is Java.")
# elif language == "C++":
#     print("Language is C++.")
# else:
#     print("No match found.")



#Boolean operators (and, or, not) are used to combine conditional statements
# user = "Admin"
# logged_in = True

# if user == "Admin" and logged_in:
#     print("Admin page")
# else:
#     print("Bad credentials")

# if not logged_in:
#     print("Please log in")  
# else:
#     print("Welcome")



# a = [1,2,3]
# b = [1,2,3]
# print(a == b) # True
# print(id(a)) # 140706982123456
# print(id(b)) # 140706982123456
# print(a is b) # False



# a = [1,2,3]
# b = a
# print(id(a)) # 140706982123456
# print(id(b)) # 140706982123456
# print(a is b) # True
# print(id(a) == id(b)) # True
# print(a == b) # True



#False,None,0,empty string,empty list,empty tuple,empty dictionary are evaluated to False   
condition = 'Test' 

if condition:
    print("Evaluated to True")
else:
    print("Evaluated to False")