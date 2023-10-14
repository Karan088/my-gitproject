print("Welcome to the Game!")
def main_menu():
    while True:
        print("Main Menu:")
        options = {
            '1': 'Option 1',
            '2': 'Option 2',
            '3': 'Option 3',
            '4': 'Exit',
        }
        for key, value in options.items():
            print(f"{key}. {value}")
        
        choice = input("Enter your choice: ")
        
        if choice == '4':
            print("Goodbye!")
            break

        selected_option = options.get(choice)
        if selected_option:
            print(f"You chose {selected_option}.")
            # Implement functionality for the selected option here
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()
