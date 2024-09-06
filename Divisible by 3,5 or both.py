for num in range(1, 101):
#Line starts loop from 1 to 100
    if num % 15 == 0:
#checks if the current number is divisble (dont use /) by 15 (both 3 and 5)
        print(num,"FizzBuzz")
    elif num % 3 == 0:
        print(num,"Fizz")
#prints fizz if num is divisble by 3 but not 5
    elif num % 5 == 0:
        print(num,"Buzz")
#prints buzz if num is divisble by 5 but not 3
    else:
        print(num,'not divisble by 3 or 5')
#if not divisble by 3 or 5 print the number itself
