def main_menu():
    while True:
        print("Main Menu:")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            option1()
        elif choice == '2':
            option2()
        elif choice == '3':
            option3()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

def option1():
    print("You chose Option 1.")
    # Implement Option 1 functionality here

def option2():
    print("You chose Option 2.")
    # Implement Option 2 functionality here

def option3():
    print("You chose Option 3.")
    # Implement Option 3 functionality here

if __name__ == "__main__":
    main_menu()
