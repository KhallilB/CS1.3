#!python


class Node(object):

    def __init__(self, data):
        """Initialize node with given data"""
        self.data = data
        self.next = None
        self.prev = None


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
        # Place before the reference
        node.next = ref

        # If node before the reference is empty
        if ref.prev is None:
            # The node becomes the new head
            self.head = node
        # Otherwise
        else:
            # Reset previous pointer of node
            node.prev = ref.prev
            # Now we point to the new node
            node.prev.next = node
        # Set the node to the node before regardless
        ref.prev = node

    def insert_after(self, ref, node):
        """Inserts a node before a given reference"""
        # Place after the refernce
        node.prev = ref

        # If the node after reference is empty
        if ref.next is None:
            # The node becomes the new tail
            self.tail = node
        # Otherwise
        else:
            # Reset the next pointer of node
            node.next = ref.next
            # Now we point to the new node
            node.next.prev = node
        # Set to the node after regardless
        ref.next = node

    def append(self, item):
        """Insert the given item at the beginning of the list"""
        # If list is empty
        if self.is_empty():
            # Node becomes the head
            self.head = item
            # Node also becomes tail because it is only item in list
            self.tail = item
        # Otherwise
        else:
            # Use helper function to insert after the tail
            self.insert_after(self.tail, item)

    def prepend(self, item):
        """ Insert the given item at the end of the list"""
        pass

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality."""
        pass

    def delete(self, item):
        """Removes an item from a linked list"""
        pass
