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
import string


num_1 = 3
num_2 = 2
print(num_1 > num_2) #This will print True because num_1 is greater than num_2
print(num_1 < num_2) #This will print False because num_1 is not less than num_2
print(num_1 >= num_2) #This will print True because num_1 is greater than or equal to num_2
print(num_1 <= num_2) #This will print False because num_1 is not less than or equal to num_2
print(num_1 == num_2) #This will print False because num_1 is not equal to num_2
print(num_1 != num_2) #This will print True because num_1 is not equal to num_2   

#casting
num_1 = '10'
num_2 = '20'
print(num_1 + num_2) #This will print 1020 because num_1 and num_2 are strings. So, they will be concatenated. This is called string concatenation.
num_1 = int(num_1) #This will convert num_1 to an integer
num_2 = int(num_2) #This will convert num_2 to an integer
print(num_1 + num_2) #This will print 30 because num_1 and num_2 are now integers. So, they will be added. This is called integer addition.