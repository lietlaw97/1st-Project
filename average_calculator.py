#created by @scherazada
#the instruction to use the program
print("""This is a Grade Calculator where you can Calculate
Your Average per quarter type "help" to show the Instructions
to use the program 
	""")

# the function for the input value and algorithm for calculating the average grade
def grade_calculator():
	name_of_user = input("Name: ")
	grade_in_math = int(input("Your Grade in Math: "))
	grade_in_eng = int(input("Your Grade in English: "))
	grade_in_fil = int(input("Your Grade in Filipino: "))
	grade_in_ap = int(input("Your Grade in AP: "))
	grade_in_sci = int(input("Your Grade in Science: "))
	grade_in_esp = int(input("Your Grade in ESP: " ))
	grade_in_tle = int(input("Your Grade in TLE: "))
	grade_in_mapeh = int(input("Your Grade in MAPEH: "))
	ave_grade = ((grade_in_math + grade_in_eng + grade_in_fil + grade_in_ap + grade_in_sci + grade_in_esp + grade_in_tle + grade_in_mapeh) / 8 )
	total_grade = (grade_in_math + grade_in_eng + grade_in_fil + grade_in_ap + grade_in_sci + grade_in_esp + grade_in_tle + grade_in_mapeh)
	if ave_grade >= 90:
		print("Total: " + str(total_grade))
		print("Your Average is: "+ str(ave_grade))
		print(name_of_user + " Congratulations!! You belong to with Honors :)")
	elif ave_grade < 75:
		print("Total: " + str(total_grade))
		print("Your Average is: "+ str(ave_grade))
		print (name_of_user + " I'm sorry but you failed :(")
	else:
		print("Total: " + str(total_grade))
		print(name_of_user + " Your average is: " + str(ave_grade))


#the control flow and commands for the program
try:
	options = ""
	while True:	
		options = input(">> ")
		if options == "help" or options == "Help":
			print("""help - to show the instructions
about - to show the copyright law and contact information
start - to start the program
quit - to exit the program
				""")
		elif options == "about" or options == "About":
			print("""Copyright 1999-2020 by Refsnes Data. All Rights Reserved.
Contact me on scherazada@protonmail.com""")
		elif options == "start" or options == "Start":
			grade_calculator()		
			while True:
				retry = input("Do you want to try again? y/n: ")
				if retry == "y" or retry == "Y":
					grade_calculator()
				elif retry == "n" or retry == "N":
					break
				else:
					print("Please choose the right options")
		elif options == "quit" or options == "exit":
			print("bye, bye :)")
			break 
		else:
			print("I don't understand please enter the right command")			
except:	
	print("Error:204 Please enter the right command or value")
############################################COMPLETED#######################################################################################
