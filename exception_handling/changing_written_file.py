#Notebook: Changing the written file.

'''
Also the other continuous project, the notebook, has relied on user actions in the sense that 
it would have broken down if the user had decided to read the file without writing anything to it. 
In this exercise we fix this, and add the possiblity of changing the used notebook file while the program is 
running.

First of all, make the program start by checking if there is a file "notebook.txt" and 
create one if there is none. If this has to be done, 
also inform the user with the warning "No default notebook was found, created one.".

When this feature works, add a fourth selection to the notebook, "(4) Change the notebook". 
If the user selects this option, the user is prompted for a new file "Give the name of the new file: ". 
If there is an existing file, it is opened and loaded into the notebook program, 
while the old notebook file is closed. If the new notebook file does not exist, 
the system informs the user "No notebook with that name detected, created one." and makes a new file. 
Also add a note of the used notebook file to the main menu, "Now using file [filename]".
If everything is implemented correctly, the program works as follows:
		
>>> 
No default notebook was found, created one.
Now using file notebook.txt
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit

Please select one: 2
Write a new note: Buy milk.
Now using file notebook.txt
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit

Please select one: 4
Give the name of the new file: otherbook.txt
No notebook with that name detected, created one.
Now using file otherbook.txt
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit

Please select one: 2
Write a new note: Buy pineapples.
Now using file otherbook.txt
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit

Please select one: 4
Give the name of the new file: notebook.txt
Now using file notebook.txt
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit

Please select one: 1
Buy milk.:::12:05:23 04/25/11

Now using file notebook.txt
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Change the notebook
(5) Quit

Please select one: 5
Notebook shutting down, thank you.
>>> 

The best way to approach the required changes in this exercise is to first rewrite the code so that it stores the name of the used notebook file in a variable, and that this variable is changed as needed. Also, the easiest way of testing if a file exists is to open it to a file handle inside exception handler. If an IOError was generated, then there was no file with that name and write mode can be used to create such file.
'''

import time

userinput = ""

while True:
	try:
		myfile=open("notebook.txt","r")
	except IOError:
		print("No default notebook was found, created one.")
		notebook="notebook.txt"
		myfile=open(notebook,"w")
	else:
		print("Now using file "+notebook+"\n(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Change the notebook\n (5) Quit\n")
		userinput = input("Please select one: ")
		if userinput == "1":
			myfile = open(notebook,"r")
			content = myfile.read()
			print(content)
			myfile.close()
		elif userinput == "2":
			myfile = open(notebook, "a")
			addedtext = input("Write a new note: ")
			addedtext = addedtext + ":::" + time.strftime("%X %x")
			myfile.write(addedtext)
			myfile.close()
		elif userinput == "3":
			myfile = open(notebook, "w")
			print("Notes deleted." + ":::" + time.strftime("%X %x"))
			myfile.close()
		elif userinput == "4":
			notebook=input("Give the name of the new file: ")
			try:
				myfile=open(notebook,"r")
			except IOError:
				print("No notebook with that name detected, created one.")
				mylife=open(notebook,"w")
				
		elif userinput == "5":
			False
			print("Notebook shutting down, thank you.")
			myfile.close()
			break