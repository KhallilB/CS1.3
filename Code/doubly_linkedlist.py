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
        # Increase the size
        self.size += 1

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
        # Increase the size
        self.size += 1

    def append(self, item):
        """Insert the given item at the beginning of the list"""
        # Create node
        node = Node(item)

        # If list is empty
        if self.is_empty():
            # Node becomes the head
            self.head = node
            # Node also becomes tail because it is only item in list
            self.tail = node
            # Increase the size
            self.size += 1
        # Otherwise
        else:
            # Use helper function to insert after the tail
            self.insert_after(self.tail, node)

    def preppend(self, item):
        """ Insert the given item at the end of the list"""
        # Create node
        node = Node(item)

        # If the list is empty
        if self.is_empty():
            # Node beceomes the head
            self.head = node
            # Node also becomes tail because it is only item in list
            self.tail = node
            # Increase the size
            self.size += 1
        # Otherwise
        else:
            # Use helper function to insert befor the head
            self.insert_before(self.head, node)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality."""
        # Start at the head
        node = self.head
        # Check to see if we found correct quality
        found = False

        # While not found
        while node and not found:
            # If the node is of the correct value
            if node.data == quality:
                # Found
                found = True
            # Otherwise
            else:
                # Move to the next node
                node = node.next

        return node

    def delete(self, item):
        """Removes an item from a linked list"""
        # Start at the head
        node = self.head
        # Check if we found item
        found = False

        # While the next node has data in i
        while node and not found:
            # If the node is of the correct value
            if node.data == item:
                # Found
                found = True
            # Otherwise
            else:
                # Move to the next node
                node = node.next

        if node.next is not None:
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            if node.data == item:
                node.prev.next = None
            else:
                raise ValueError('Item not found')

    def traverse(self):
        """"Navigates through all the items in the linked list"""
        if self.is_empty():
            raise ValueError('List is emopty')
            return
        else:
            node = self.head
            while node is not None:
                print(node.data, " ")
                node = node.next


def test_doubly_linked_list():
    ll = DoublyLinkedList()
    print('Appending Items:')
    ll.append('A')
    ll.append('B')
    ll.append('C')
    ll.traverse()
    print('Preappending Items:')
    ll.preppend('1')
    ll.preppend('2')
    ll.preppend('3')
    ll.traverse()
    print('Deleting Items:')
    ll.delete('1')
    ll.delete('2')
    ll.delete('3')
    ll.traverse()


if __name__ == '__main__':
    test_doubly_linked_list()
