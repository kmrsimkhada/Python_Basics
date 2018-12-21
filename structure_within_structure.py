#Structures within structures
'''
The second exercise takes another step towards more realistic programming structures. 
In this exercise the idea is to create an if-structure, which has another if-structure inside it.

The idea is to create a program which asks for a user name and password. 
If the given name is wrong, the program prints "The given name is wrong". 
If the name is acceptable, the program asks for the password. 
If the password is correct, the system prints "Both inputs are correct!", otherwise "The password is incorrect.". 
The correct inputs should be "John" and the password "ABC123". 

'''

str1 = input("Give name: ")

if str1 == "John":
	str2 = input("Give password: ")
	
	if str2 == "ABC123":
		print("Both inputs are correct!")
	else:
		print("The password is incorrect.")

else:
	print("The given name is wrong.")