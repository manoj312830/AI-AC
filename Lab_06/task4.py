def sum(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total

# Example usage
num = int(input("Enter a number: "))
print(f"Sum of first {num} numbers using for loop: {sum(num)}")

