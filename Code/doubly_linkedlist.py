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
