class Node:
    """
    A node in a linked list used for Stack implementation.
    """

    def __init__(self, data):
        """
        Initialize a node with data and next pointer.

        Args:
            data: The data to be stored in the node.
        """
        self.data = data
        self.next = None


class StackNode:
    """
    A stack data structure implementation using linked list.

    This class provides methods for creating and manipulating a stack.

    Functions available:
    - push(data): Pushes an item onto the top of the stack.
    - pop(): Removes and returns the top item from the stack.
    - peek(): Returns the top item from the stack without removing it.
    - is_empty(): Checks if the stack is empty.
    - size(): Returns the number of items in the stack.
    - traverse(): Traverses and prints all elements in the stack.
    - clear(): Clears all elements from the stack.
    - duplicate_top(): Duplicates the top element of the stack.
    """

    def __init__(self):
        """
        Initialize an empty stack.
        """
        self.top = None
        self._size = 0

    def push(self, data):
        """
        Push an item onto the top of the stack.

        Args:
            data: The data to be pushed onto the stack.
        """
        new_node = Node(data)
        new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The top item from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            top_data = self.top.data
            self.top = self.top.next
            self._size -= 1
            return top_data
        else:
            raise IndexError("pop from empty stack")

    def peek(self):
        """
        Return the top item from the stack without removing it.

        Returns:
            The top item from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.top.data
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return self.top is None

    def size(self):
        """
        Return the number of items in the stack.

        Returns:
            The number of items in the stack.
        """
        return self._size

    def traverse(self):
        """
        Traverse and print all elements in the stack.
        """
        current = self.top
        while current:
            print(current.data)
            current = current.next

    def clear(self):
        """
        Clear all elements from the stack.
        """
        self.top = None
        self._size = 0

    def duplicate_top(self):
        """
        Duplicate the top element of the stack.
        """
        if not self.is_empty():
            top_data = self.peek()
            self.push(top_data)

    # Add more methods as needed...
