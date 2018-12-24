#Notebook: Read and write to the notebook

'''
The last exercise in this chapter is the first part of the second multi-part assignment of this course, 
the notebook. 
In this notebook the user is able to add, read and delete notes from a separate note file "notebook.txt".


Create a program which allows the user to 
(1) Read the contents of the notebook
(2) Add notes to the file or
(3) Delete all of the notes. 
If the user selects 1, the entire notebook file is printed to the screen, 
if 2 then the program prompts "Write a new note: ", 
and adds the written note as the last line into the file with a trailing line break "\n". 
If the player selects 3, the file is emptied and the message "Notes deleted" will be shown. 
Also add the option (4) Quit, which ends the program, printing "Notebook shutting down, thank you.". 
With other selections the program prompts "Incorrect selection". When working, the program prints following:

>>> 
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Buy new tires
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 2
Write a new note: Buy new headlights
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 1
Buy new tires
Buy new headlights

(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 3
Notes deleted.
(1) Read the notebook
(2) Add note
(3) Empty the notebook
(4) Quit

Please select one: 4
Notebook shutting down, thank you.
>>>  
'''
readfile = open("notebook.txt", "w")

while True:
	
	print("(1) Read the notebook\n(2) Add note\n(3) Empty the notebook\n(4) Quit\n")
	select = input("Please select one :")
	
	if select == "1":
		readfile = open("notebook.txt", "r")
		content = readfile.readlines()
		
		if len(content) == 0:
			readfile = open("notebook.txt", "a")
			readfile.write("Buy milk\n")
			readfile = open("notebook.txt", "r")
			content = readfile.readlines()
			
			for i in content:
				print(i[:-1])
			
			readfile.close()
			
		else:
			
			for i in content:
				print(i[:-1])
			
			readfile.close()
		
	elif select == "2":
		readfile = open("notebook.txt", "a")
		note = input("Write a new note: ")
		readfile.write(note+"\n")
		readfile.close()
	
	elif select == "3":
		readfile == open("notebook.txt", "w")
		readfile.close()
		print("Notes deleted.")
		
	elif select == "4":
		print("Notebook shutting down, thank you.")
		break;
	
