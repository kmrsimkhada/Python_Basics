#Basic Subfunctions

'''
The first assignment in this chapter is easy: create a program with a main function and a separate subfunction called hello, which when called prints "Hello there!". 
The subfunction does not take any parameters or return any value, just prints the line. 
Then, to the main function, add a call to the subfunction and two print commands, the first one before the call which says "Lets call the subfunction:", and one after the subfunction call, a print command which prints "Quitting.". 
If implemented correctly, the program will print the following:

>>> 
Lets call the subfunction:
Hello there!
Quitting.
>>> 

'''
def subfunction():
	
	print("Hello there!")
	

def main():
	
	print("Lets call the subfunction:")
	subfunction()
	print("Quitting.")
	
	
if __name__ == "__main__":
    main()