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
greeting = 'Hello'
name = 'John'
message = greeting + ', ' + name + '. Welcome!'
print(message)
message = '{}, {}. Welcome!'.format(greeting, name) #This is a better way to format the message
print(message)
message = f'{greeting}, {name.upper()}. Welcome!' #This is the best way to format the message. This is call f strings.
print(message)

#To getting help with working with strings, we can use the dir() and help() functions. The dir() function will return a list of all the methods available for the string class. The help() function will return a description of the string class and its methods.
#print(dir(name)) #This will print all the methods available for the string class    
#print(help(str)) #This will print all the methods available for the string class with description
#print(help(str.lower)) #This will print the description of the lower method