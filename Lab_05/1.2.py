import getpass
import hashlib

def hash_password(password):
    """Hash the password using SHA-256."""
    return hashlib.sha256(password.encode()).hexdigest()

def mask_email(email):
    """Mask the email address for privacy."""
    parts = email.split('@')
    if len(parts) != 2:
        return "invalid_email"
    return parts[0][0] + "***@" + parts[1]

def mask_phone(phone):
    """Mask the phone number for privacy."""
    return "*" * (len(phone) - 2) + phone[-2:]

def collect_user_data():
    """Collect user data from input."""
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    email = input("Enter your email: ")
    phone = input("Enter your phone number: ")
    address = input("Enter your address: ")
    return {
        "name": name,
        "age": age,
        "email": mask_email(email),
        "phone": mask_phone(phone),
        "address": address
    }

def save_data_to_file(data, password_hash, filename="userdata.txt"):
    """Save anonymized user data and password hash to a file."""
    with open(filename, "w") as f:
        f.write("# User data (anonymized)\n")
        for key, value in data.items():
            f.write(f"{key}: {value}\n")
        f.write("# Password hash for access\n")
        f.write(f"password_hash: {password_hash}\n")

def main():
    print("Welcome! Please create a password to protect your data.")
    password = getpass.getpass("Create a password: ")
    confirm_password = getpass.getpass("Confirm password: ")
    if password != confirm_password:
        print("Passwords do not match. Exiting.")
        return
    password_hash = hash_password(password)
    print("Now, please enter your details.")
    user_data = collect_user_data()
    save_data_to_file(user_data, password_hash)
    print("Your data has been saved and protected with your password.")

if __name__ == "__main__":
    main()