#Complete if-structure
'''
The third exercise is to create a conditional structure which prints a line depending on the given selection. 
The program asks a number between 1 and 3, and based on the number prints the following: 
1 prints "You selected one.", 2 prints "You selected two." and 3 prints "You selected three.", 
like this:

Select a number (1-3): 1
You selected one.

'''

number  = int(input("Select a number (1-3):"))
if(number == 1):
	print("You selected one.")
elif(number == 2):
	print("You selected two.")
elif(number == 3):
	print("You selected three.")