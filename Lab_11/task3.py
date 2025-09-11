class Node:
    def __init__(self, data):
        self.data = data
        self.next = None  # Pointer to the next node

class LinkedList:
    def __init__(self):
        self.head = None  # Start with an empty list

    def insert_at_end(self, data):
        """Insert a new node with the given data at the end of the list."""
        new_node = Node(data)
        if self.head is None:
            # If the list is empty, new node becomes the head
            self.head = new_node
        else:
            current = self.head
            # Traverse to the last node
            while current.next:
                current = current.next
            # Set the next pointer of the last node to the new node
            current.next = new_node

    def delete_value(self, value):
        """Delete the first node with the specified value."""
        current = self.head
        prev = None
        while current:
            if current.data == value:
                if prev is None:
                    # Deleting the head node: move head pointer to next node
                    self.head = current.next
                else:
                    # Bypass the current node by updating the previous node's next pointer
                    prev.next = current.next
                return True  # Value found and deleted
            prev = current
            current = current.next
        return False  # Value not found

    def traverse(self):
        """Traverse the list and return a list of node values."""
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next  # Move to the next node
        return elements

# --- Inline Comments on Pointer Updates ---
# - In insert_at_end, when adding a new node, we update the 'next' pointer of the last node to point to the new node.
# - In delete_value, if deleting the head, we update 'self.head' to point to the next node.
#   If deleting a middle or last node, we update 'prev.next' to skip the current node and point to 'current.next'.

# --- Suggested Test Cases ---
if __name__ == "__main__":
    ll = LinkedList()
    # Test 1: Insert into empty list
    ll.insert_at_end(10)
    print("After inserting 10:", ll.traverse())  # [10]

    # Test 2: Insert more elements
    ll.insert_at_end(20)
    ll.insert_at_end(30)
    print("After inserting 20, 30:", ll.traverse())  # [10, 20, 30]

    # Test 3: Delete head
    ll.delete_value(10)
    print("After deleting 10 (head):", ll.traverse())  # [20, 30]

    # Test 4: Delete middle element
    ll.insert_at_end(40)
    ll.delete_value(30)
    print("After deleting 30 (middle):", ll.traverse())  # [20, 40]

    # Test 5: Delete last element
    ll.delete_value(40)
    print("After deleting 40 (last):", ll.traverse())  # [20]

    # Test 6: Delete non-existent value
    result = ll.delete_value(99)
    print("Attempt to delete 99 (not in list):", result, ll.traverse())  # False, [20]

    # Test 7: Delete only remaining element
    ll.delete_value(20)
    print("After deleting 20 (only element):", ll.traverse())  # []

    # Test 8: Traverse empty list
    print("Traverse empty list:", ll.traverse())  # []

