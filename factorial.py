'''
Python program to find the factorial of a number provided by the user.
For example, the factorial of 6 (denoted as 6!) is 1*2*3*4*5*6 = 720. 
Factorial is not defined for negative numbers and the factorial of zero is one, 0! = 1.
'''

num = int(input("Enter a number: "))

factorial = 1

# check if the number is negative, positive or zero
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("The factorial of",num,"is",factorial)