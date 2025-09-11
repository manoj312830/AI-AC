class Stack:
    """A simple Stack (LIFO) implementation in Python.

    Methods:
        push(item): Add an item to the top of the stack.
        pop(): Remove and return the top item of the stack.
        peek(): Return the top item without removing it.
        is_empty(): Return True if the stack is empty, False otherwise.
    """

    def __init__(self):
        """Initialize an empty stack."""
        self._items = []

    def push(self, item):
        """Add an item to the top of the stack.

        Args:
            item: The item to be added.
        """
        self._items.append(item)

    def pop(self):
        """Remove and return the top item of the stack.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self._items.pop()

    def peek(self):
        """Return the top item without removing it.

        Returns:
            The item at the top of the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        """Check if the stack is empty.

        Returns:
            bool: True if the stack is empty, False otherwise.
        """
        return len(self._items) == 0

# Test stack operations using sample data
if __name__ == "__main__":
    stack = Stack()
    print("Is stack empty?", stack.is_empty())
    stack.push(10)
    stack.push(20)
    stack.push(30)
    print("Top of stack (peek):", stack.peek())
    print("Pop:", stack.pop())
    print("Pop:", stack.pop())
    print("Is stack empty?", stack.is_empty())
    print("Pop:", stack.pop())
    print("Is stack empty?", stack.is_empty())
    # Uncommenting the next line will raise an error
    # print("Pop from empty stack:", stack.pop())

    # Suggestion: For optimized performance (especially for large stacks),
    # consider using collections.deque, which provides O(1) time complexity
    # for append and pop operations from both ends.
    #
    # Example alternative implementation:
    # from collections import deque
    # class Stack:
    #     def __init__(self):
    #         self._items = deque()
    #     def push(self, item):
    #         self._items.append(item)
    #     def pop(self):
    #         return self._items.pop()
    #     def peek(self):
    #         return self._items[-1]
    #     def is_empty(self):
    #         return not self._items
