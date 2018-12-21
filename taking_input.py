#Calculator, taking an input
'''
In this exercise, the objective is to try taking input for the first time. 
The idea is to create a simple program which takes two numbers and perfoms an addition. 
So, take two numbers from the user with input(), calculate the result and make the program present the result in the following way:

Calculator
Give the first number: 100
Give the second number: 25
The result is: 125

In this exercise it is OK to expect that the user wont give faulty inputs, 
such as strings or something else non-calculatable. 
This exercise is also the starting point for the course's two "on-going" exercises, meaning that this code will be supplemented with new features in the future. 
Therefore it may be worthwhile to start commenting the source code.
'''

print("Calculator")
val1 = int(input("Give the first number:"))
val2 = int(input("Give the second number:"))
print("The result is: "+str(val1+val2))