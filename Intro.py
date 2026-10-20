#Print Welcome Message
# message = 'Hello World'
# print(message)
# print(len(message))
# print(message[0])
# print(message[10])
# print(message[0:5])
# print(message[6:11])

#methods
# print(message.upper())
# print(message.lower())
# print(message.count('Hello')) #There is only one Hello in the message so it returns 1
# print(message.find('World')) #This returns 6 because world is starting with 6th index

# #replace
# new_message = message.replace('World', 'Universe') #This replaces World with Universe
# print(new_message)

#string formatting
# greeting = 'Hello'
# name = 'John'
# message = greeting + ', ' + name + '. Welcome!'
# print(message)
# message = '{}, {}. Welcome!'.format(greeting, name) #This is a better way to format the message
# print(message)
# message = f'{greeting}, {name.upper()}. Welcome!' #This is the best way to format the message. This is call f strings.
# print(message)

#To getting help with working with strings, we can use the dir() and help() functions. The dir() function will return a list of all the methods available for the string class. The help() function will return a description of the string class and its methods.
#print(dir(name)) #This will print all the methods available for the string class    
#print(help(str)) #This will print all the methods available for the string class with description
#print(help(str.lower)) #This will print the description of the lower method

#intergers and variables
# num1 = 3
# print(type(num1)) #This will print the type of the variable num1 which is int
# num2 = 4.5
# print(type(num2)) #This will print the type of the variable num2 which is float 
# print(3 + 2) #This will print the sum of num1 and num2 which is 7.5   
# print(3 - 2) #This will print the difference of num1 and num2 which is 0.5
# print(3 * 2) #This will print the product of num1 and num2 which is 6
# print(3 / 2) #This will print the quotient of num1 and num2 which is 1.5
# print(3 // 2) #This will print the floor division of num1 and num2 which is 1
# print(3 % 2) #This will print the remainder of num1 and num2 which is 1. We call this modulus operator. It is used to find the remainder of a division operation.
# print(2 % 2) #This will print the remainder of num1 and num2 which is 0. We call this modulus operator. It is used to find the remainder of a division operation. 
# print(3 ** 2) #This will print the power of num1 and num2 which is 9    
# print(3 + 2 * 5) #This will print the sum of num1 and num2 which is 13. This is because multiplication has a higher precedence than addition. So, 2 * 5 is evaluated first and then added to 3. 
# print(abs(-3)) #This will print the absolute value of num1 which is 3. The abs() function is used to find the absolute value of a number. It returns the positive value of a number.
# print(round(3.7)) #This will print the rounded value of num1 which is 4. The round() function is used to round a number to the nearest integer. It returns the nearest integer value of a number.   
# print(round(3.27,1)) #This will print the rounded value of num1 which is 3.3 because requested the first didgit.

#Use comparisons for numbers
num_1 = 3
num_2 = 2
print(num_1 > num_2) #This will print True because num_1 is greater than num_2
print(num_1 < num_2) #This will print False because num_1 is not less than num_2
print(num_1 >= num_2) #This will print True because num_1 is greater than or equal to num_2
print(num_1 <= num_2) #This will print False because num_1 is not less than or equal to num_2
print(num_1 == num_2) #This will print False because num_1 is not equal to num_2
print(num_1 != num_2) #This will print True because num_1 is not equal to num_2     
