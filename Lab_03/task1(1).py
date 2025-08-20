 
def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def get_and_print_factorial():
    try:
        num = int(input("Enter a non-negative integer: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"Factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Please enter a valid integer.")

if __name__ == "__main__":
    get_and_print_factorial()