class Node:
    """
    A Node class for representing elements in a linked list-based queue.
    """
    def __init__(self, data):
        """
        Initialize a new Node with the given data.

        Args:
            data: The data to be stored in the Node.
        """
        self.data = data
        self.next = None


class Queue:
    """
    A queue data structure implementation using linked list.

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
        self.front = None
        self.rear = None

    def enqueue(self, item):
        """
        Add an item to the rear of the queue.

        Args:
            item: The item to be added to the queue.
        """
        new_node = Node(item)
        if self.is_empty():
            self.front = new_node
        else:
            self.rear.next = new_node
        self.rear = new_node

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
        front_data = self.front.data
        if self.front == self.rear:
            self.rear = None
        self.front = self.front.next
        return front_data

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
        return self.front.data

    def is_empty(self):
        """
        Check if the queue is empty.

        Returns:
            True if the queue is empty, False otherwise.
        """
        return self.front is None

    def size(self):
        """
        Return the number of items in the queue.

        Returns:
            The number of items in the queue.
        """
        count = 0
        current = self.front
        while current:
            count += 1
            current = current.next
        return count

    def traverse(self):
        """
        Traverse and print all elements in the queue.
        """
        current = self.front
        while current:
            print(current.data)
            current = current.next

    def clear(self):
        """
        Clear all elements from the queue.
        """
        self.front = None
        self.rear = None

    # Add more methods as needed...
