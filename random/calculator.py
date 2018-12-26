#Calculator: math-library

'''
This exercise expands on the calculator, which was made in chapter 4, exercise 4. 
In this exercise, add sin() and cos() -calculations from the library module math to the calculator. 
Add these actions as selections 5 and 6, simultaneously moving the "change numbers" feature to 7 and "Quit" to 8. 
When the user calls either of the new features, the first number is the divident and second the divider like this: 
sin(number_1/number2). When correctly implemented, the program prints the following:
			
>>> 

Calculator
Give the first number: 1
Give the second number: 2
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 1 2
Please select something (1-6): 5
The result is: 0.479425538604203
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 1 2
Please select something (1-6): 6
The result is: 0.8775825618903728
(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit
Current numbers: 1 2
Please select something (1-6): 8
Thank you!
>>> 

'''
import math

def main():
	print("Calculator")
	num1 = int(input("Give the first number: "))
	num2 = int(input("Give the second number: "))
	
	while True:
		print("""(1) +
(2) -
(3) *
(4) /
(5)sin(number1/number2)
(6)cos(number1/number2)
(7)Change numbers
(8)Quit""")
		print("Current numbers: ",num1," ", num2)
		selection = int(input("Please select something (1-6): "))
		if selection == 1:
			result = num1 + num2
			print("The result is: ",result)
		elif selection == 2:
			result = num1 - num2
			print("The result is: ",result)
		elif selection == 3:
			result = num1 * num2
			print("The result is: ",result)
		elif selection == 4:
			result = num1 / num2
			print("The result is: ",result)
		elif selection == 5:
			result = math.sin(num1/num2)
			print("The result is: ",result)
		elif selection == 6:
			result = math.cos(num1/num2)
			print("The result is: ",result)
		elif selection == 7:
			num1 = int(input("Give the first number: "))
			num2 = int(input("Give the second number: "))
		elif selection == 8:
			print("Thank you!")
			break

			
if __name__ == "__main__":
	main()
