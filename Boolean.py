name = input('what is your name? ' )
number = input(f"Hello {name}, please enter your identification number. ")

while True:
    verify = input(f'Kindly verify your identification number: {number}. Type Yes if it\'s correct. Otherwise, type No. ')

    if verify.lower() == 'yes':
        break
    elif verify.lower() == 'no':
        number = input(f"Please re-enter your identification number. ")
    else:
        print("Invalid input. Please enter 'Yes' or 'No'.")

print("Verification successful.")

