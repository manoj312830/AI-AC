

# Fix: sort_list will sort numbers before strings, but mixed types cause TypeError in Python 3.
# To sort consistently, convert all items to strings for comparison.
def sort_list_consistent(data):
    return sorted(data, key=str)

items = [3, "apple", 1, "banana", 2]
print(sort_list_consistent(items))
