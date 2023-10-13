def main_menu():
    print("Main Menu:")
    print("1. Option 1")
    
    choice = input("Enter your choice (1 to select option, or 'q' to quit): ")
    
    if choice == '1':
        option1()
    elif choice.lower() == 'q':
        print("Goodbye!")
    else:
        print("Invalid choice. Please try again.")

def option1():
    print("You chose Option 1.")
    # Implement Option 1 functionality here

if __name__ == "__main__":
    main_menu()
