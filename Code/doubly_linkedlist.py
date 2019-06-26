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

    def insert_empty_list(self, item):
        """If the list is empty insert node at the start of linked list"""
        # If the list is empty
        if self.is_empty():
            # Create new node
            node = Node(item)
            # Make the new node the head node
            self.head = node
            # Increase the size
            self.size += 1
        else:
            raise ValueError('List is Empty')

    def append(self, item):
        """Insert the given item at the beginning of the list"""
        # If the head is empty:
        if self.is_empty:
            # Create new node
            node = Node(item)
            # Created node becomes new head node
            self.head = node
            # Exit
            return
        # Otherwise if its not empty
        # Create new node
        node = Node(item)
        # Point the head to the next node
        node.next = self.head
        # Point the node back toward the head
        self.head.previous = node
        # Head becomes the new node
        self.head = node

    def prepend(self, item):
        """ Insert the given item at the end of the list"""
        pass

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality."""
        pass

    def delete(self, item):
        """Removes an item from a linked list"""
        pass
