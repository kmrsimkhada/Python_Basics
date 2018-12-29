#Creating a class and an object

'''
The first exercise is related to basic class definition. Create a program which has a class Player, which has two attributes, teamcolor and points. 
Then create a main function which creates an object from this class, gives its attributes values "Blue" and "300". 
After this, make the program print the object data in the form "The [color] contender has [points] points!" like this:
		
>>> 
The Blue contender has 300 points!
>>> 		

'''

class Player:
	
	teamcolor = ""
	points = ""

def main():
	
	randomstuff = Player()
	randomstuff.teamcolor = "Blue"
	randomstuff.points = 300
	
	print("The ",randomstuff.teamcolor," contender has ",randomstuff.points, " points!")
	
	
	
if __name__ == "__main__":
    main()