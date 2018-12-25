#Nuke-Foot-cockroach

'''
The second exercise in this chapter continues with random selection. 
In this exercise the objective is to develop a game called nuke-foot-cockroach, which is pretty similar to the more popular variant, paper-rock-scissors. 
The rules are simple: both players select either nuke, foot or cockroach, and the winner is determined in the following way: 
Foot beats cockroach, nuke beats foot and cockroach beats nuke. 
If both the player and the AI select the same, it's a tie, except if both choose nuke, then both lose.

Implement the game so that the other player is computer controlled, and chooses randomly either foot(number 1), cockroach(number 3) or nuke(number 2).
 Also implement a feature which keeps the score, calculating both rounds the player won, and ties. 
 If the player wins, print "You WIN!", if they loose "You LOSE!". 
 If the round was a tie, either "It is a tie!" or "Both LOSE!", depending on if the tie was caused by a nuke or not.
 If the player selects "quit", the game ends and the final score is given. 
 When the game works correctly, it prints the following:
 
 >>> 
Foot, Nuke or Cockroach? (Quit ends): Nuke
You chose: Nuke
Computer chose: Foot
You WIN!
Foot, Nuke or Cockroach? (Quit ends): Nuke
You chose: Nuke
Computer chose: Nuke
Both LOSE!
Foot, Nuke or Cockroach? (Quit ends): Cockroach
You chose: Cockroach
Computer chose: Nuke
You WIN!
Foot, Nuke or Cockroach? (Quit ends): Foot
You chose: Foot
Computer chose: Nuke
You LOSE!
Foot, Nuke or Cockroach? (Quit ends): Spaceshuttle
Incorrect selection.
Foot, Nuke or Cockroach? (Quit ends): Foot
You chose: Foot
Computer chose: Nuke
You LOSE!
Foot, Nuke or Cockroach? (Quit ends): Quit
You played 5 rounds, and won 2 rounds, playing tie in 0 rounds.
>>>  
'''

import random

	
def userchoice():
	
	u_choice = str(input("Foot, Nuke or Cockroach? (Quit ends): "))
	
	if u_choice == "Foot":
		print("You chose: Foot")
		return 1
	
	elif u_choice =="Nuke":
		print("You chose: Nuke")
		return 2
	
	elif u_choice =="Cockroach":
		print("You chose: Cockroach")
		return 3
	
	elif u_choice =="Quit":
		return 4
	
	else:
		return 5
	
def computerchoice():
	
	comp_choice = random.randint(1,4)
	
	if comp_choice == 1:
		
		print("Computer chose: Foot")
		
	elif comp_choice == 2:
		
		print("Computer chose: Nuke")
	
	elif comp_choice == 3:
		
		print("Computer chose: Cockroach")
	
	return comp_choice
	
def main():
	
	rounds = 0
	win = 0
	ties =0
	
	while True:
		
		usernumber = userchoice()
		
		if usernumber == 4:
			print("You played ", rounds ," rounds, and won ",win," rounds, playing tie in ",ties,"rounds.")
			break
		if usernumber == 5:
			print("Incorrect selection.")
			usernumber = userchoice()
		
		compnumber = computerchoice()
		
		if usernumber == 1 and compnumber == 3 or usernumber == 2 and compnumber == 1 or usernumber == 3 and compnumber == 2:
			print("You WIN!")
			win = win+1
		
		elif compnumber == 1 and usernumber == 3 or compnumber == 2 and usernumber == 1 or compnumber == 3 and usernumber == 2:
			print("You LOSE!")
		
		elif usernumber == compnumber:
			if usernumber ==2 and compnumber ==2:
				print("Both LOSE!")
			else:
				print("It is a tie!")
				ties = ties+1
		
		rounds = rounds+1
	
if __name__=="__main__":
	main()