from pyfiglet import Figlet
from time import sleep
import random


info = Figlet(font='big')
print(info.renderText('Rock Paper Scissors\nGame'))
def resulttext():
	info = Figlet(font='big')
	print(info.renderText('Result'))


#oyun hakkında bilgi verelim
print("""
----------------OYUN HAKKINDA BİLGİLER------------------
-TR-
Taş için 'rock' yazmanız gereklidir
Makas için 'scissors' yazmanız gereklidir
Kağıt için 'paper' yazmanız gereklidir

-EN-
rock
scissors
paper

 ! you have to choose the word you want and write it that way !
  """)

def computer_random():
	number=random.randint(1,3)
	if number==1:
		return "rock"
	elif number==2:
		return "paper"
	else:
		return "scissors"
computerscore=0
myscore=0
while True:
	print("_____________________________________")
	print("\n")
	userselection=input("rock paper scissors ? :")
	print("_____________________________________")
	resulttext()
	print("-------------------------------------")
	print("User         : {} ".format(userselection))
	print("\n")
	computerrandom=computer_random()
	print("Computer     : ",computerrandom)
	print("-------------------------------------")

	if userselection==computerrandom:
		print("Draw Score")
		print("My Score       :{}".format(myscore))
		print("Computer Score :{}".format(computerscore))

	elif userselection=="rock" and computerrandom=="scissors":
		print("You WON !...")
		myscore=myscore+1
		print("My Score       :{}".format(myscore))
		print("Computer Score :{}".format(computerscore))

	elif userselection=="rock" and computerrandom=="paper":
		print("the computer won...")
		computerscore=computerscore+1
		print("My Score       :{}".format(myscore))
		print("Computer Score :{}".format(computerscore))

	elif userselection=="scissors" and computerrandom=="paper":
		print("You WON !...")
		myscore=myscore+1
		print("My Score       :{}".format(myscore))
		print("Computer Score :{}".format(computerscore))

	elif userselection=="scissors" and computerrandom=="rock":
		print("the computer won...")
		computerscore=computerscore+1
		print("My Score       :{}".format(myscore))
		print("Computer Score :{}".format(computerscore))

	elif userselection=="paper" and computerrandom=="rock":
		print("You WON !...")
		myscore=myscore+1
		print("My Score       :{}".format(myscore))
		print("Computer Score :{}".format(computerscore))

	elif userselection=="paper" and computerrandom=="scissors":
		print("the computer won...")
		computerscore=computerscore+1
		print("My Score       :{}".format(myscore))
		print("Computer Score :{}".format(computerscore))
	else:
		print("YOU ENTERED THE WRONG WORD !")




