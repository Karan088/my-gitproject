print("Even or Odd & Prime Number Checker")

try:
    number = int(input("Enter a number:"))

    if number % 2 == 0:
        print(number, "is even.")
    else:
        print(number, "is odd.")

    if number > 1:
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                print(number, "is not a prime number.")
                break
        else:
            print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

except ValueError:
    print("Invalid input. Please enter a valid integer.")
