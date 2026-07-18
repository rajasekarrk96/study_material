class Queue:
    """
    A queue data structure implementation using a list.

    Functions available:
    - enqueue(item): Add an item to the rear of the queue.
    - dequeue(): Remove and return the front item from the queue.
    - peek(): Return the front item from the queue without removing it.
    - is_empty(): Check if the queue is empty.
    - size(): Return the number of items in the queue.
    - traverse(): Traverse and print all elements in the queue.
    - clear(): Clear all elements from the queue.
    """

    def __init__(self):
        """
        Initialize an empty queue.
        """
        self.items = []

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.

        Args:
            item: The item to be added to the queue.
        """
        self.items.append(item)

    def dequeue(self):
        """
        Remove and return the front item from the queue.

        Returns:
            The front item from the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        """
        Return the front item from the queue without removing it.

        Returns:
            The front item from the queue.

        Raises:
            IndexError: If the queue is empty.
        """
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return len(self.items) == 0

    def size(self):
        """
        Return the number of items in the queue.

        Returns:
            The number of items in the queue.
        """
        return len(self.items)

    def traverse(self):
        """
        Traverse and print all elements in the queue.
        """
        for item in self.items:
            print(item)

    def clear(self):
        """
        Clear all elements from the queue.
        """
        self.items = []

    # Add more methods as needed...
