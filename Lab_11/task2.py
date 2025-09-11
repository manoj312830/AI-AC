# Queue implementation using Python lists
class QueueList:
    def __init__(self):
        self._items = []

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.pop(0)

    def is_empty(self):
        return len(self._items) == 0

# Optimized queue implementation using collections.deque
from collections import deque

class QueueDeque:
    def __init__(self):
        self._items = deque()

    def enqueue(self, item):
        self._items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self._items.popleft()

    def is_empty(self):
        return len(self._items) == 0

# Performance Review:
"""
Performance Comparison:
- The list-based queue (QueueList) uses list.append() for enqueue (O(1)), but dequeue uses pop(0), which is O(n) because all elements must be shifted.
- The deque-based queue (QueueDeque) uses collections.deque, which provides O(1) time complexity for both append (enqueue) and popleft (dequeue) operations.
- For large queues or frequent dequeue operations, QueueDeque is significantly more efficient and is the recommended implementation for queue data structures in Python.
"""

# Example usage
if __name__ == "__main__":
    print("Testing QueueList:")
    ql = QueueList()
    ql.enqueue(1)
    ql.enqueue(2)
    ql.enqueue(3)
    print("Dequeue:", ql.dequeue())
    print("Is empty?", ql.is_empty())
    print("Dequeue:", ql.dequeue())
    print("Dequeue:", ql.dequeue())
    print("Is empty?", ql.is_empty())

    print("\nTesting QueueDeque:")
    qd = QueueDeque()
    qd.enqueue(1)
    qd.enqueue(2)
    qd.enqueue(3)
    print("Dequeue:", qd.dequeue())
    print("Is empty?", qd.is_empty())
    print("Dequeue:", qd.dequeue())
    print("Dequeue:", qd.dequeue())
    print("Is empty?", qd.is_empty())
