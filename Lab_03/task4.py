def user_system():
    users = {}  # Dictionary to store username:password pairs

    while True:
        print("\n--- User System ---")
        print("1. Register")
        print("2. Login")
        print("3. Exit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '1':
            username = input("Enter a username to register: ").strip()
            if username in users:
                print("Username already exists. Please choose another.")
            else:
                password = input("Enter a password: ").strip()
                users[username] = password
                print("Registration successful!")

        elif choice == '2':
            username = input("Enter your username: ").strip()
            password = input("Enter your password: ").strip()
            if username in users and users[username] == password:
                print("Login successful! Welcome,", username)
            else:
                print("Invalid username or password.")

        elif choice == '3':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":
    user_system()
