#Notebook: Adding dates to the system

'''
The last exercise in this chapter adds a small feature to the other continuous exercise project, the notebook. 
In this exercise, add a feature which includes the date and time of the written note to the program. 
The program works as earlier, but saves data in the form "[note]:::[date and time]" meaning that there is a three-colon separator between the note and timestamp. 
The timestamp can be generated as follows:
	
>>> import time		

>>> time.strftime("%X %x")
'19:01:34 01/03/09'
>>> 

This returns the date and time in a nice, compact string. When working correctly, the program prints the following:
			
>>> 
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Call mom.
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 1
Call mom.:::11:44:41 04/25/11

(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 4
Notebook shutting down, thank you.
>>> 

'''
import time

userinput = ""
keepgoing = True
while keepgoing:
	print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit")
	userinput = input("Please select one: ")
	if userinput == "1":
		myfile = open("notebook.txt","r")
		content = myfile.read()
		print(content)
		myfile.close()
	elif userinput == "2":
		myfile = open("notebook.txt", "a")
		addedtext = input("Write a new note: ")
		addedtext = addedtext + ":::" + time.strftime("%X %x")
		myfile.write(addedtext)
		myfile.close()
	elif userinput == "3":
		myfile = open("notebook.txt", "w")
		print("Notes deleted." + ":::" + time.strftime("%X %x"))
		myfile.close()
	elif userinput == "4":
		keepgoing = False
		print("Notebook shutting down, thank you.")
		myfile.close()
	else:
		print("Wrong input")