print("Even or Odd, Prime, and Circle Perimeter Checker")

try:
    choice = int(input("Choose an option:\n1. Even or Odd\n2. Prime or Not\n3. Circle Perimeter\nEnter the corresponding number: "))

    if choice == 1:
        number = int(input("Enter a number:"))
<<<<<<< HEAD
        result = "even" if number % 2 == 0 else "odd"
        print(f"{number} is {result}.")
    elif choice == 2:
        number = int(input("Enter a number:"))
        if number > 1:
            is_prime = all(number % i != 0 for i in range(2, int(number**0.5) + 1))
            prime_status = "a prime" if is_prime else "not a prime"
            print(f"{number} is {prime_status} number.")
        else:
            print(f"{number} is not a prime number.")
=======
        if number % 2 == 0:
            print(number, "is even.")
        else:
            print(number, "is odd.")
    elif choice == 2:
        number = int(input("Enter a number:"))
        if number > 1:
            for i in range(2, int(number ** 0.5) + 1):
                if number % i == 0:
                    print(number, "is not a prime number.")
                    break
            else:
                print(number, "is a prime number.")
        else:
            print(number, "is not a prime number.")
>>>>>>> 2c51f36bb9352c6d6baa4ebc01bd6f1ee5a81a5d
    elif choice == 3:
        radius = float(input("Enter the radius of the circle:"))
        perimeter = 2 * 3.14159 * radius
        print(f"The perimeter of the circle with radius {radius} is {perimeter:.2f}.")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
except ValueError:
    print("Invalid input. Try Again later.")
print( "Thank YOU! COME AGAIN :))

