print("Even or Odd Number Checker :Try Now")

try:
    number = int(input("Enter a number:"))

    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
