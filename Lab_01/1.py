
def find_maximum(numbers):
    return max(numbers)

# Read 3 elements from the user
user_input = []
for i in range(3):
    num = float(input(f"Enter element {i+1}: "))
    user_input.append(num)

maximum = find_maximum(user_input)
print("The maximum element is:", maximum)