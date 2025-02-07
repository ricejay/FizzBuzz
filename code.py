for n in range(100):
    if (n % 15 == 0):
        print("FizzBuzz") # Print FizzBuzz if both number is divisible by 3 and 5
    elif (n % 3 == 0):
        print("Fizz") # Print Fizz if number is divisible by 3
    elif (n % 5 == 0):
        print("Buzz") # Print Buzz if number is divisible by 5
    else:
        print(n) # Else print the number itself
