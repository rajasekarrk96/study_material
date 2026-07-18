class StackList:
    """
    A stack data structure implementation.

    This class provides methods for creating and manipulating a stack.

    Functions available:
    - push(item): Pushes an item onto the top of the stack.
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
        self.items = []

    def push(self, item):
        """
        Push an item onto the top of the stack.

        Args:
            item: The item to be pushed onto the stack.
        """
        self.items.append(item)

    def pop(self):
        """
        Remove and return the top item from the stack.

        Returns:
            The top item from the stack.

        Raises:
            IndexError: If the stack is empty.
        """
        if not self.is_empty():
            return self.items.pop()
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
            return self.items[-1]
        else:
            raise IndexError("peek from empty stack")

    def is_empty(self):
        """
        Check if the stack is empty.

        Returns:
            True if the stack is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of items in the stack.

        Returns:
            The number of items in the stack.
        """
        return len(self.items)

    def traverse(self):
        """
        Traverse and print all elements in the stack.
        """
        for item in reversed(self.items):
            print(item)

    def clear(self):
        """
        Clear all elements from the stack.
        """
        self.items = []

    def duplicate_top(self):
        """
        Duplicate the top element of the stack.
        """
        if not self.is_empty():
            top_item = self.peek()
            self.push(top_item)

    # Add more methods as needed...
