def print_multiples_for(n):
    print(f"First 10 multiples of {n} using for loop:")
    for i in range(1, 11):
        print(f"{n}*{i}={n*i}")

# Example usage
num = int(input("Enter a number: "))
print_multiples_for(num)
