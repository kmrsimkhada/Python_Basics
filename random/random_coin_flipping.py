#Random module, Coin flipping

'''
The first exercise in this chapter consists of simple module library operations. 
In the chapter, a module called random was introduced. 
This module consists of several functions which can be used to get random numbers. 
The idea here is to create a program, which simulates coin flips by randomly selecting 0 (Tails) or 1 (Heads) and printing out the result. 
When working correctly, the program prints out something like this:

>>> 
Heads!
'''

import random

if random.randint(0,1) == 1:
	print("Heads!")
	
else:
	print("Tails!")
