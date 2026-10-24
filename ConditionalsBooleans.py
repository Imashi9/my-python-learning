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
user = "Admin"
logged_in = True

# if user == "Admin" and logged_in:
#     print("Admin page")
# else:
#     print("Bad credentials")

if not logged_in:
    print("Please log in")  
else:
    print("Welcome")