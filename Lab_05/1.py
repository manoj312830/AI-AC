# This script collects user data and stores it in a '.txt' file

# Prompt the user for their information
name = input("Enter your name: ")
age = input("Enter your age: ")
email = input("Enter your email: ")
phone = input("Enter your phone number: ")
address = input("Enter your address: ")

# Prepare the data to be written to the file
user_data = (
    f"Name: {name}\n"
    f"Age: {age}\n"
    f"Email: {email}\n"
    f"Phone: {phone}\n"
    f"Address: {address}\n"
)

# Open a text file in write mode (creates the file if it doesn't exist)
with open("user_data.txt", "w") as file:
    # Write the user data to the file
    file.write(user_data)

# Inform the user that the data has been saved
print("User data has been saved to 'user_data.txt'.")




