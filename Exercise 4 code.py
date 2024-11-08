# Question 1: Using a for loop with a list

# # TODO: Create a list of fruits
list = ("banana" , "peach" , "kiwi")

# # TODO: Use a for loop to print each fruit in the list
for list in list:
    print(list)
#-------------------------------------------------------------------------
# Question 2: Using a while loop for countdown

# TODO: Use a while loop to create a countdown from 5 to 1
count =5
while count >0:
    print(count)
    count -=1


#-------------------------------------------------------------------------
# Question 3: Using a for loop with range()

# TODO: Use a for loop to print the first 10 square numbers
i = 1

for i in range (1,11):
    print(i*i)
#-------------------------------------------------------------------------

# Question 4: Using the random module

# TODO: Import the random module
import random
# TODO: Create a list of colors
list = ["pink" , "black", "orange", "blue", "red", "yellow"]

# TODO: Use a for loop to select and print 3 random colors from the list
for random_list in range (3):

    random_list = random.choice(list)
    print(random_list)

    
#-------------------------------------------------------------------------
# Question 5: Creating and using a custom module

# TODO: Create a new file named 'math_operations.py' with the following content:
a= int(input("enter first number"))
b= int(input("enter second number"))

operation = input("insert an operation of your choice, +,-,*,/")

while true:
    
   if operation == "+":
        print (a+b)
        result = a + b 


   elif operation == "-":
        print (a-b)
        result = a - b


   elif operation == "*":
       print (a*b)
       result = a * b


   elif b != 0 and operation == "/":
        print (a / b)
   else:
    print("Error: Division by zero")



# TODO: Import the custom module and use its functions
import math_operations as MO

(MO.add(2,3))
(MO.subtract(5,2))
(MO.multiply(2,5))
(MO.divide(10,2))


# TODO: Use a while loop to create a simple calculator
print(result)