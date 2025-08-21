def classify(age):
    if age<0:
        return "invalid age";
    elif age<=12:
        return "child";
    elif age<=19:
        return "teen";
    elif age<=59:
        return "adult";
    else:
        return "Senior";
user_age = int(input("Enter your age: "))
print(f"You are classified as: {classify(user_age)}")
    