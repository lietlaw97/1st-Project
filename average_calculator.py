#@scherazade
#IMPORTING SLEEP FUNCTION FROM TIME MODULE
from time import sleep

print('TYPE "help" TO SHOW INSTRUCTIONS')
#LIST FOR SUBJECTS
subjects = ['Math', 'English', 'Science', 'Filipino', 'AP', 'ESP', 'TLE', 'MAPEH']
#FUNCTION FOR THE ALGORITHM
def main(total = 0):
	name_of_user = input('Name: ')
	#A FOR LOOP FOR GETTING THE INPUT FOR THE USER AND CALCULATING THE AVERAGE
	for sub in subjects:
		grade = int(input(f'Enter Grade in {sub}: '))
		total += grade
		ave_grade = total / 8
	print("Calculating....")
	sleep(1.3)
	if ave_grade >= 90:
		print(f'Total: {total}')
		sleep(0.65)
		print(f'Average: {ave_grade}\nCongratulations!! {name_of_user}')
	elif ave_grade < 75:
		print(f'Total: {total}')
		sleep(0.65)
		print(f"Average: {ave_grade}\nI'm sorry {name_of_user} you failed :( try again next time")
	else:
		print(f"Total: {total}")
		sleep(0.65)
		print(f'Average: {ave_grade}')

#FUNCTIONS FOR CONTROL FLOW AND COMMANDS FOR THE PROGRAM
def control_flow():
	while True:	
		options = input(">> ")
		if options == "help":
			print("""NOTE:ALL COMMANDS MUST BE IN LOWERCASE
about - to show the copyright law and contact information
start - to start the program
quit - to exit the program
				""")
		elif options == "about":
			print("""Copyright 1999-2020 by Refsnes Data. All Rights Reserved.
Contact me on scherazada@protonmail.com""")
		elif options == "start":
			main()
			while True:
				sleep(0.5)
				retry = input("Do you want to try again? y/n: ")
				if retry == "y" or retry == "Y":
					main()
				elif retry == "n" or retry == "N":
					break
				else:
					print("Please choose the right options")
		elif options == "quit":
			print("bye, bye :)")
			exit()
		else:
			print("I don't understand please enter the right command")

try:
	if __name__ == '__main__':
		control_flow()
		main()
		sleep(5)
except ValueError:
	print("Error: ValueError")
	exit()
