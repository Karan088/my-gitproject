print("Even or Odd, Prime, and Circle Perimeter Checker")

try:
    choice = int(input("Choose an option:\n1. Even or Odd\n2. Prime or Not\n3. Circle Perimeter\nEnter the corresponding number: "))

    if choice == 1:
        number = int(input("Enter a number:"))
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
    elif choice == 3:
        radius = float(input("Enter the radius of the circle:"))
        perimeter = 2 * 3.14159 * radius
        print(f"The perimeter of the circle with radius {radius} is {perimeter:.2f}.")
    else:
        print("Invalid choice. Please choose 1, 2, or 3.")
except ValueError:
    print("Invalid input. Try Again later.")

