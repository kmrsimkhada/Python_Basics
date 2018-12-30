#Notebook: Using list with the notebook, pickle

'''
As this is the last exercise for procedural programming, this exercise is also a sort of final 
project, which implements all of the things discussed during the course. 
Also, even this if this exercise is marked as an exercise for the continuing notebook program, 
the changes made in the program will be rather excessive, 
so it may be a good idea to start from a clean plate.


In this exercise the idea is to build a notebook which applies the Python data structure list 
as a note manipulation method when the program is executed, 
and saves the data in a bitwise mode with pickle. The program has the following features:
A) It is possible to add notes, with similar timestamps as earlier. 
B)It is possible to edit a note by selecting it from the list, and rewriting it with new data.
C) It is possible to delete notes separately based on the selection and 
D) Notebook loads an existing notebook file from the file "notebook.dat" if such a file exists.


When the program starts, the system should check for a notebook datafile "notebook.dat" 
and load it with pickle. If no such file exists, 
or there was a problem with the file, a new file is created and the user is 
notified "No default notebook was found, created one.". 
After this the basic main menu works as in the earlier notebook:
	
>>> 
No default notebook was found, created one.
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 2
Write a new note: Buy birdseed.
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 1
Buy birdseed.:::16:41:40 04/25/11


If the user is not pleased with a note, it is possible to change one note with the option 3. 
Then the program asks for the edited note (0 is the first one on the list) with the 
prompt "The list has [number] notes.\nWhich of them will be changed?:". 
After giving an input, the user is then printed the selected note and asked for a new 
note "Give the new note:". This new note replaces the old note on the list:

(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 3
The list has 1 notes.
Which of them will be changed?: 0
Buy birdseed.:::16:41:40 04/25/11
Give the new note: Buy pig food.
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 1
Buy pig food.:::16:42:03 04/25/11

Deleting a note is done similarly as editing. The only real difference is that the deleted 
note is printed to the user with the notification "Deleted note [deleted note]".

(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 4
The list has 1 notes.
Which of them will be deleted?: 0
Deleted note Buy pig food.:::16:42:03 04/25/11

Finally, when the user decides to quit, the current notebook is saved as a datagram 
to the file "notebook.dat", with the notification "Notebook shutting down, thank you.".

(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 5
Notebook shutting down, thank you.

Also, if there already is a notebook datagram file, it should be loaded at startup, 
and otherwise normally used in the notebook program:
	
>>> 

(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 1
Buy gas:::16:45:51 04/25/11
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 4
The list has 1 notes.
Which of them will be deleted?: 0
Deleted note Buy gas:::16:45:51 04/25/11
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 2
Write a new note: Call tow truck
(1) Read the notebook
(2) Add note
(3) Edit a note
(4) Delete a note
(5) Save and quit

Please select one: 5
Notebook shutting down, thank you.
>>> 

This program is probably the most difficult exercise in this course, but it is possible to implement it 
with roughly 50 to 60 lines of code when applying the things taught during this course.
When you get this program to work, it is time to congratulate yourself, as that means that you have 
been able to use most, if not all, of the main topics from this course efficiently!
'''
# -*- coding: cp1252 -*-


import time
import pickle

notefile = "notebook.dat"
notelist = []
try:
    handle = open(notefile,"rb")
    notelist = pickle.load(handle)
    handle.close()
except Exception:
    print("No default notebook was found, created one.")
    handle = open(notefile,"w")
    handle.close()

while True:
    print("(1) Read the notebook\n(2) Add note\n\
(3) Edit a note\n(4) Delete a note\n(5) Save and quit\n")
    selection = int(input("Please select one: "))
    if selection == 1:
        for i in notelist:
            print(i)
    elif selection == 2:
        newnote = input("Write a new note: ")
        timestamp = time.strftime("%X %x")
        notelist.append(newnote+":::"+timestamp)
    elif selection == 3:
        print("The list has",len(notelist),"notes.")
        changenote = int(input("Which of them will be changed?: "))-1
        print(notelist[changenote])
        uusi = input("Give the new note: ")
        timestamp = time.strftime("%X %x")
        notelist[changenote] = uusi+":::"+timestamp
    elif selection == 4:
        print("The list has",len(notelist),"notes.")
        deleteme = int(input("Which of them will be deleted?: "))-1
        deletednote = notelist.pop(deleteme)
        print("Deleted note",deletednote)
    elif selection == 5:
        savedata = open(notefile,"wb")
        pickle.dump(notelist,savedata)
        savedata.close()
        print("Notebook shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")