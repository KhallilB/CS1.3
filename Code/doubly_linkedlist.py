#!python


class Node(object):

    def __init__(self, data):
        """Initialize node with given data"""
        self.data = data
        self.next = None
        self.previous = None


class DoublyLinkedList(object):

    def __init__(self, iterable=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First Node
        self.tail = None  # Last Node
        self.size = 0  # Number of nodes
        # Append the given items
        if iterable is not None:
            for item in iterable:
                self.append(item)

    def is_empty(self):
        """Return True if this linked list is empty, or False if not empty."""
        return self.head is None

    def insert_before(self, ref, node):
        """Inserts a node after a given reference"""

    def insert_after(self, ref, node):
        """Inserts a node before a given reference"""
        pass

    def append(self, item):
        """Insert the given item at the beginning of the list"""
        pass

    def prepend(self, item):
        """ Insert the given item at the end of the list"""
        pass

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality."""
        pass

    def delete(self, item):
        """Removes an item from a linked list"""
        pass
