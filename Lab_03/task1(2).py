
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def get_factorial_from_user():
    try:
        num = int(input("Enter a number to calculate its factorial: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Invalid input. Please enter an integer.")

# To run the function:
if __name__ == "__main__":
    get_factorial_from_user()

