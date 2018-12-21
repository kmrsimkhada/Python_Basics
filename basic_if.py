#The basic if-structure
'''
The exercises of the third chapter, as well as the third chapter itself, focus on the conditional if-structure. 
In the first exercise the objective is to create a simple if-structure. 
The program should first ask a number from the user and save it to a variable. 
Then if the number is even (possible to divide by 2), the program should print the text "The given number was even.". 
The best way to do this is to use the operator remainder. 
The program should print the following:

Give a number: 24
The given number was even.

or alternatively

Give a number: 11

Meaning that the program should not print anything if the number is odd.
'''

value= int(input("Give a number: "))
if(value%2==0):
	print("The given number was even.")
