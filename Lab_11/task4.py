class Node:
    """
    Node class for Binary Search Tree.

    Attributes:
        key (int): The value stored in the node.
        left (Node): Left child node.
        right (Node): Right child node.
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

class BST:
    """
    Binary Search Tree implementation.

    Methods:
        insert(key): Inserts a key into the BST.
        search(key): Returns True if key is in the BST, else False.
        inorder_traversal(): Returns a list of keys in inorder.
    """
    def __init__(self):
        self.root = None

    def insert(self, key):
        """
        Insert a key into the BST.

        Args:
            key (int): The value to insert.
        """
        def _insert(node, key):
            if node is None:
                return Node(key)
            if key < node.key:
                node.left = _insert(node.left, key)
            elif key > node.key:
                node.right = _insert(node.right, key)
            # If key == node.key, do not insert duplicates
            return node

        self.root = _insert(self.root, key)

    def search(self, key):
        """
        Search for a key in the BST.

        Args:
            key (int): The value to search for.

        Returns:
            bool: True if key is found, False otherwise.
        """
        def _search(node, key):
            if node is None:
                return False
            if key == node.key:
                return True
            elif key < node.key:
                return _search(node.left, key)
            else:
                return _search(node.right, key)
        return _search(self.root, key)

    def inorder_traversal(self):
        """
        Perform inorder traversal of the BST.

        Returns:
            list: List of keys in inorder.
        """
        result = []
        def _inorder(node):
            if node:
                _inorder(node.left)
                result.append(node.key)
                _inorder(node.right)
        _inorder(self.root)
        return result

# Test the BST implementation
if __name__ == "__main__":
    bst = BST()
    nums = [7, 3, 9, 1, 5, 8, 10]
    for num in nums:
        bst.insert(num)

    print("Inorder Traversal:", bst.inorder_traversal())  # Should be sorted

    # Test search for present and absent elements
    test_values = [5, 10, 2, 11]
    for val in test_values:
        found = bst.search(val)
        print(f"Search {val}: {'Found' if found else 'Not Found'}")
