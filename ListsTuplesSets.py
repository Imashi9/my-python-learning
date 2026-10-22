#Lists
# courses = ["History", "Math", "Physics", "CompSci"]
# courses_2 = ["Art", "Education"]
# print(courses)
# print(len(courses)) #This will print the length of the list courses which is 4
# print(courses[0]) #This will print the first element of the list courses which is
# print(courses[-1]) #This will print the last element of the list courses which is CompSci
# print(courses[0:2]) #This will print the first two elements of the list
# print(courses[2:]) #This will print the elements of the list from index 2 to the end

#courses.append("Art") #This will add the element "Art" to the end of the
#print(courses)

#courses.insert(0, "Art") #This will add the element "Art" to the beginning of the list
#print(courses)
#courses.insert(0, courses_2) #This will add the list courses_2 to the beginning of the list courses
#print(courses)

# courses.extend(courses_2) #This will add the elements of the list courses_2 to the end of the list courses
# print(courses)

# courses.remove("Math") #This will remove the element "Math" from the list courses
# print(courses)

# courses.pop() #This will remove the last element of the list courses
# print(courses)

#courses.reverse() #This will reverse the order of the elements in the list courses
#print(courses)

# numbers = [1, 5, 2, 4, 3]
# numbers.sort() #This will sort the elements of the list numbers in ascending order
# print(numbers)
# numbers.sort(reverse=True) #This will sort the elements of the list numbers in descending order
# print(numbers)

# print(min(numbers)) #This will print the minimum value of the list numbers
# print(max(numbers)) #This will print the maximum value of the list numbers
# print(sum(numbers)) #This will print the sum of the elements of the list numbers

# print('Math' in courses) #This will print True if the element "Math" is in the list courses, otherwise it will print False  

# for course in courses: #This will iterate through the elements of the list courses and print each element
#     print(course)

# for course in enumerate(courses): #This will iterate through the elements of the list courses and print the index and the element
#     print(course)

# for course in enumerate(courses, start=1): #This will iterate through the elements of the list courses and print the index and the element starting from 1
#     print(course)

# courses_str = ', '.join(courses) #This will join the elements of the list courses into a string separated by a comma and a space
# print(courses_str)

# new_list = courses_str.split(', ') #This will split the string courses_str into a list of elements separated by a comma and a space
# print(new_list)

#Tuples
# tuple_1 = ("History", "Math", "Physics", "CompSci")
# tuple_2 = tuple_1

# print(tuple_1)
# print(tuple_2)

#Sets

courses = {"History", "Math", "Physics", "CompSci"}
courses_2 = {"Art", "Education", "Math"}
print(courses)
print('Math' in courses) #This will print True if the element "Math" is in the set courses, otherwise it will print False   
print(courses.intersection(courses_2)) #This will print the elements that are common to both sets courses and courses_2
print(courses.difference(courses_2)) #This will print the elements that are in
print(courses.union(courses_2)) #This will print the elements that are in either set courses or courses_2

#Note: Sets are unordered collections of unique elements. They do not support indexing, slicing, or other sequence-like behavior.
empty_list = []
empty_list = list() #This will create an empty list
empty_tuple = ()
empty_tuple = tuple() #This will create an empty tuple
empty_set = {} #This will create an empty dictionary
empty_set = set() #This will create an empty set