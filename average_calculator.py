# @scherazade
# IMPORTING SLEEP FUNCTION FROM TIME MODULE TO CREATE THE DELAY EFFECT
from time import sleep

print('TYPE "help" TO SHOW INSTRUCTIONS')

SUBJECTS = [
    "Math",
    "English",
    "Science",
    "Filipino",
    "AP",
    "ESP",
    "TLE",
    "MAPEH",
]  # LIST OF SUBJECTS


def main(total=0):
    name_of_user = input("Name: ")
    gradeSubject = []
    # A FOR LOOP FOR ASKING THE USER'S GRADE IN EACH SUBJECT AND STORE IT IN "gradeSubject" LIST OR ARRAY
    for sub in SUBJECTS:
        grade = int(input(f"Enter Grade in {sub}: "))
        gradeSubject.append(grade)
        total += grade
        aveGrade = total / 8

    # AN INFINITE LOOP TO ASK THE USER IF HE/SHE WANTS TO SAVE THEIR GRADE IN A TEXT FILE
    # THE INFINITE LOOP WILL ONLY BREAK IF THE PROGRAM FINISHED SAVING THEIR GRADE OR IF THE USER TYPE "N or n"
    while True:
        saveInput = input("Do you want to save your grade? y/n: ")
        if saveInput == "Y" or saveInput == "y":
            fileName = input("Please enter filename: ")
            if len(fileName) > 20:
                print("\nERROR:CHARACTER LIMIT EXCEEDED NO MORE THAN 20 CHARACTERS\n")
                break
            print("Saving....")
            sleep(0.6), print(f"Successfully saved to {fileName}.txt\a")
            savingInput = open(f"{fileName}.txt", "w")
            savingInput.write(f"Name: {name_of_user}\n\n")
            for subject, grade in zip(SUBJECTS, gradeSubject):
                savingInput.write(f"{subject}: {grade}\n")
            break
        else:
            break
    print("\nCalculating....")
    sleep(1.3)
    if aveGrade >= 90:
        print(f"Total: {total}")
        sleep(0.65)
        print(f"Average: {aveGrade}\nCongratulations!! {name_of_user}")
    elif aveGrade < 75:
        print(f"Total: {total}")
        sleep(0.65)
        print(
            f"Average: {aveGrade}\nI'm sorry {name_of_user} you failed :( try again next time"
        )
    return print(f"Total: {total}"), sleep(0.65), print(f"Average: {aveGrade}")


# THE FUNCTION FOR THE CONSOLE TO ENTER THEIR COMMANDS
def commands():
    # ANOTHER INFINITE LOOP TO CREATE THE CONSOLE TO ENTER THE USER'S COMMANDS
    while True:
        options = input(">> ".strip())
        # IF THE USER ENTER "help" THE CONSOLE WILL PRINT ALL THE POSSIBLE COMMANDS
        if options == "help":
            print(
                """NOTE:ALL COMMANDS MUST BE IN LOWERCASE
about - to show the copyright law and contact information
start - to start the program
quit - to exit the program"""
            )
        # IF THE USER ENTER "about" THE CONSOLE WILL PRINT THE CONTACT DETAILS AND COPYRIGHT LAW
        elif options == "about":
            print(
                """Copyright 1999-2020 by Refsnes Data. All Rights Reserved.
Contact me on scherazada@protonmail.com"""
            )
        # IF THE USER ENTER "start" THE PROGRAM WILL CALL THE MAIN FUNCTION AND START THE PROGRAM
        elif options == "start":
            main()
            # AN INFINITE LOOP TO ASK THE USER IF THEY WANT TO RESTART THE PROGRAM
            while True:
                sleep(0.5)
                retry = input("Do you want to try again? y/n: ")
                if retry == "y" or retry == "Y":
                    main()
                else:
                    break
        elif options == "quit":  # IF THE USER ENTER "quit" THE PROGRAM WILL TERMINATE
            print("bye, bye :)")
            exit()
        else:
            print(
                "I don't understand please enter the right command"
            )  # IF THE USER TYPE NONESENSE THE CONSOLE WILL PRINT THIS


# CALLING THE TWO FUNCTION AND THE DELAYED EFFECT
try:
    if __name__ == "__main__":
        commands()
        main()
# IF THE USER ENTER NOTHING TO THE CONSOLE THE EXCEPT STATEMENT WILL PRINT AN ERROR
except ValueError:
    print("Error: ValueError")
    exit()
