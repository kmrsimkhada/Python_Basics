#Calculator: Checking input validity

'''
The third exercise in the chapter continues with the calculator exercises done earlier. 
This time the idea is to finally take out the annoying problems with numbers, input validity and the stability problems caused by type conversion funvtion.

Make the following changes to the calculator: 
Every time the user gives numbers to the program, the system asks for the numbers with the prompt 
"Give a number: " and continues until a valid number is given. If the number is not correct, 
the system gives an error message "This input is invalid.". If the calculator works correctly, 
it prints out the following:
		
>>> 
Calculator
Give a number: hah, NEVER
This input is invalid.
Give a number: What?
This input is invalid.
Give a number: 100
Give a number: Just kidding
This input is invalid.
Give a number: 50
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 100 50
Please select something (1-6): 2
The result is: 50
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 100 50
Please select something (1-6): 8
Thank you!
>>> 

The easiest way of implementing this feature is probably to define a separate function to call when asking 
numbers. In this function, an iteration keeps asking a number as long as the user decides to joke around. 
If the input is valid, iteration terminates with break and the function returns an acceptable value.
'''

import math

print("Calculator")


while True:
	try:
		num1 = input("Give a number: ")
		num1 = int(num1)
		break
		
	except ValueError:
		print("This input is invalid.")
		
while True:
	try:
		num2 = input("Give a number: ")
		num2 = int(num2)
		break
		
	except ValueError:
		print("This input is invalid.")

while True:	
	print("(1) +\n(2) -\n(3) *\n(4) /\n(5) sin(number1/number2)\n(6) cos(number1/number2)\n(7) Change numbers\n(8) Quit\n")
	print("Current numbers:" , num1,num2)
	value = int(input("Please select something (1-6): "))
	if value == 1:
		print("The result is:" ,num1+num2)
	elif value == 2:
		print("The result is:" ,num1-num2)
	elif value == 3:
		print("The result is:" ,num1*num2)
	elif value == 4:
		print("The result is:" ,num1/num2)
	elif value == 5:
		print("The result is:" , math.sin(num1/num2))
	elif value == 6:
		print("The result is:" , math.cos(num1/num2))
	elif value == 7:
		while True:
			try:
				num1=input("Give a number: ")
				num1=int(num1)
			except ValueError:
				print("This input is invalid.")
				
		while True:
			try:
				num2=input("Give a number: ") 
				num2=int(num2)
			except ValueError:
				print("This input is invalid.")
		
	elif value == 8:
		print("Thank you!")
		False
		break