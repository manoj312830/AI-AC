def get_and_sort_numbers():
    try:
        nums_input = input("Enter numbers separated by spaces: ")
        nums = [float(x) for x in nums_input.strip().split()]
        nums.sort()
        print("Sorted numbers:", nums)
        return nums
    except ValueError:
        print("Invalid input. Please enter only numbers separated by spaces.")
        return []

if __name__ == "__main__":
    get_and_sort_numbers()
