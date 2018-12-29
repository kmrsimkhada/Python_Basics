#More list methods

'''
The third exercise also revolves around list methods, this time doing data manipulation. 
In the same folder as the source code, there is a file named "words.txt", which has a randomly selected set of words. 
Build a program, which reads all of the words from the file, sorts them in alphabetic order and prints out the list with the statement "Words in an alphabetical order:". 
When correctly implemented, the program prints out the following:
		
>>> 
Words in an alphabetical order:
aardvark
beercase
buzz
hammer
house
lion
nail
roadworks
salesman
shovel
table
xenon
>>> 

All the words in the file are written in lowercase letters, and do not have any special characters or numbers.
'''

readfiles = open("words.txt", "r")
content = readfiles.readlines()
myList = content
myList.sort()
print("Words in an alphabetical order:")

for i in myList:
	print(i)
