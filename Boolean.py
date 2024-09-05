name = input('what is your name? ' )
number = input(f"Hello {name}, please enter your identification number. ")
#Ask for name and ID for some organization/company

while True:
    verify = input(f'Kindly verify your identification number: {number}. Type Yes if it\'s correct. Otherwise, type No. ')
#Verify if inputted value is true or false
    if verify.lower() == 'yes':
        break
#If inputted yes it breaks the loop
    elif verify.lower() == 'no':
        number = input(f"Please re-enter your identification number. ")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")
#Loop repeats asking them for correct ID number

print("Verification successful.")

