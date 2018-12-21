#Using several parameters
'''
In this exercise the idea is to define an if-structure which decides the action based on several inputs. 
The program asks for two numbers. If both of the numbers are even, the program prints "Both numbers are even." If only one of the numbers is even, the program prints "One of the numbers is even.". 
Finally, if neither of the numbers is even, the program prints "Both numbers are odd".

'''

number1 = int(input("Give a number: "))
number2 = int(input("Give another number: "))


if number1%2==1 and number2%2 ==1:
	print("Both numbers are odd.")
	
elif number1%2==0 and number2%2==0:
	print("Both numbers are even.")
	
else:
	print("One of the numbers is even.")