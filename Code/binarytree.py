#!python
from queue import Queue
from stack import Stack


class BinaryTreeNode(object):

    # Balaced Tree - Binary tree where each leaf is the same distance from the root

    def __init__(self, data):
        """Initialize this binary tree node with the given data."""
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        """Return a string representation of this binary tree node."""
        return 'BinaryTreeNode({!r})'.format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        # TODO: Check if both left child and right child have no value
        return self.left is None and self.right is None

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        # TODO: Check if either left child or right child has a value
        return False if self.is_leaf() else True

    def height(self):
        """Return the height of this node (the number of edges on the longest
        downward path from this node to a descendant leaf node).
        Runtime: Best case: O(log(n)) Worst Case: O(n) where n is the number of items in the tree"""
        left_height = 0
        right_height = 0

        if self.is_leaf():
            return 0

        if self.left is not None and self.right is not None:
            return 1 + max(self.left.height(), self.right.height())
        elif self.left is not None:
            return 1 + self.left.height()
        elif self.right is not None:
            return 1 + self.right.height()


class BinarySearchTree(object):

    def __init__(self, items=None):
        """Initialize this binary search tree and insert the given items."""
        self.root = None
        self.size = 0
        if items is not None:
            for item in items:
                self.insert(item)

    def __repr__(self):
        """Return a string representation of this binary search tree."""
        return 'BinarySearchTree({} nodes)'.format(self.size)

    def is_empty(self):
        """Return True if this binary search tree is empty (has no nodes)."""
        return self.root is None

    def height(self):
        """Return the height of this tree (the number of edges on the longest
        downward path from this tree's root node to a descendant leaf node).
        Best Case: O(log(n)) Worst case: O(n) Where n is the amount of items in the tree"""
        # TODO: Check if root node has a value and if so calculate its height
        if self.root is not None:
            return self.root.height()
        else:
            return 0

    def contains(self, item):
        """Return True if this binary search tree contains the given item.
        Best case running time: O(log(n)) 
        Worst case running time: O(n) Where (n) is the amount of items in the tree"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # Return True if a node was found, or False
        return node is not None

    def search(self, item):
        """Return an item in this binary search tree matching the given item,
        or None if the given item is not found.
        Best case running time: O(log(n)) 
        Worst case running time: O(n) Where (n) is the amount of items in the tree"""
        # Find a node with the given item, if any
        node = self._find_node_recursive(item, self.root)
        # TODO: Return the node's data if found, or None
        return node.data if node is not None else None

    def insert(self, item):
        """Insert the given item in order into this binary search tree.
        Best case running time: O(log(n)) 
        Worst case running time: O(n) Where (n) is the amount of items in the tree"""
        # Handle the case where the tree is empty
        if self.is_empty():
            # TODO: Create a new root node
            self.root = BinaryTreeNode(item)
            # TODO: Increase the tree size
            self.size += 1
            return
        # Find the parent node of where the given item should be inserted
        parent = self._find_parent_node_recursive(item, self.root)
        # TODO: Check if the given item should be inserted left of parent node
        if parent.data > item:
            # TODO: Create a new node and set the parent's left child
            parent.left = BinaryTreeNode(item)
        # TODO: Check if the given item should be inserted right of parent node
        elif parent.data < item:
            # TODO: Create a new node and set the parent's right child
            parent.right = BinaryTreeNode(item)
        # TODO: Increase the tree size
        self.size += 1

    def _find_node_iterative(self, item):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed iteratively
        starting from the root node.
        Best case running time: O(log(n)) 
        Worst case running time: O(n) Where (n) is the amount of items in the tree"""
        # Start with the root node
        node = self.root
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the found node
                return node
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Descend to the node's left child
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Descend to the node's right child
                node = node.right
        # Not found
        return None

    def _find_node_recursive(self, item, node):
        """Return the node containing the given item in this binary search tree,
        or None if the given item is not found. Search is performed recursively
        starting from the given node (give the root node to start recursion).
        Best case running time: O(log(n)) of O(1) if the root node
        Worst case running time: O(n) Where (n) is the amount of items in the tree"""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return None
        # TODO: Check if the given item matches the node's data
        elif item == node.data:
            # Return the found node
            return node
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            return self._find_node_recursive(item, node.left)
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            # TODO: Recursively descend to the node's right child, if it exists
            return self._find_node_recursive(item, node.right)

    def _find_parent_node_iterative(self, item):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed iteratively starting from the root node.
        Best case running time: O(log(n))
        Worst case running time: O(n) Where (n) is the amount of items in the tree"""
        # Start with the root node and keep track of its parent
        node = self.root
        parent = None
        # Loop until we descend past the closest leaf node
        while node is not None:
            # TODO: Check if the given item matches the node's data
            if item == node.data:
                # Return the parent of the found node
                return parent
            # TODO: Check if the given item is less than the node's data
            elif item < node.data:
                # TODO: Update the parent and descend to the node's left child
                parent = node
                node = node.left
            # TODO: Check if the given item is greater than the node's data
            elif item > node.data:
                # TODO: Update the parent and descend to the node's right child
                parent = node
                node = node.right
        # Not found
        return parent

    def _find_parent_node_recursive(self, item, node, parent=None):
        """Return the parent node of the node containing the given item
        (or the parent node of where the given item would be if inserted)
        in this tree, or None if this tree is empty or has only a root node.
        Search is performed recursively starting from the given node
        (give the root node to start recursion)."""
        # Check if starting node exists
        if node is None:
            # Not found (base case)
            return parent
        # TODO: Check if the given item matches the node's data
        elif item == node.data:
            # Return the parent of the found node
            return parent
        # TODO: Check if the given item is less than the node's data
        elif item < node.data:
            # TODO: Recursively descend to the node's left child, if it exists
            # Hint: Remember to update the parent parameter
            return self._find_parent_node_recursive(item, node.left, node)
        # TODO: Check if the given item is greater than the node's data
        elif item > node.data:
            # TODO: Recursively descend to the node's right child, if it exists
            # Hint: Remember to update the parent parameter
            return self._find_parent_node_recursive(item, node.right, node)

    def _find_predecessor(self, node):
        """Returns the rightmost node of the left subtree of a given node"""
        # Navaigate a step to the left
        predecessor = node.left

        # Navigate to the right until we cant anymore
        while predecessor.right is not None:
            predecessor = predecessor.right

        # Return rightmost node
        return predecessor

    def _find_successor(self, node):
        """Returns the leftmost node of the right subtree of a given node"""
        # Navigate a step to the right
        successor = node.right

        # Navigate to the left until we cant anymore
        while successor.left is not None:
            successor = successor.left

        # Return the leftmost node
        return successor

    def delete(self, item):
        """Remove given item from this tree, if present, or raise ValueError.
        Best case running time: O(log(n))
        Worst case running time: O(n) Where (n) is the amount of items in the tree"""
        # TODO: Use helper methods and break this algorithm down into 3 cases
        # based on how many children the node containing the given item has and
        # implement new helper methods for subtasks of the more complex cases
        # Cases: Empty Tree, Value is root, Value not found, Has left child, has right child, Has both

        # Find the node
        node = self._find_node_recursive(item, self.root)
        # Find parent of node
        parent = self._find_parent_node_recursive(item, self.root)

        # If not found
        if (node is None or node.data != item):
            return

        # If is a leaf(no children)
        elif (node.is_leaf()):
            # If item is less than parent data
            if item < parent.data:
                # Set left child to None
                parent.left = None
            # Otherwise
            # If the item is greater than the parent data
            elif item > parent.data:
                # Set the right child to None
                parent.right = None

        # If node only has a left child
        elif node.left and node.right is None:
            # If item is less than parent data
            if item < parent.data:
                # Update parents left node
                parent.left = node.left
            # Otherwise
            else:
                # Update parents right node
                parent.right = node.left

        # If node only has a right child
        elif node.left is None and node.right:
            # If the item is less than the parent data
            if item < parent.data:
                # Update parents left node
                parent.left = node.right
            # Otherwise
            else:
                # Update parents right node
                parent.right = node.right

        # If the node has a left and a right child
        elif(node.is_branch()):
            pred_parent = node
            pred = self._find_predecessor(node)

            # Predecessor becomes new node
            node.data = pred.data

            # If it has a right child only
            if pred.right:
                if pred_parent.data > pred.data:
                    pred_parent.left = pred.right

                elif pred_parent.data < pred.data:
                    pred_parent.right = pred.right
            # There are no childern at all
            else:
                if pred.data < pred_parent.data:
                    pred_parent.left = None
                else:
                    pred_parent.right = None

    def items_in_order(self):
        """Return an in-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree in-order from root, appending each node's item
            self._traverse_in_order_recursive(self.root, items.append)
        # Return in-order list of all items in tree
        return items

    def _traverse_in_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node is None:
            return

        # TODO: Traverse left subtree, if it exists
        self._traverse_in_order_recursive(node.left, visit)
        # TODO: Visit this node's data with given function
        visit(node.data)
        # TODO: Traverse right subtree, if it exists
        self._traverse_in_order_recursive(node.right, visit)

    def _traverse_in_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative in-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse in-order without using recursion (stretch challenge)
        stack = Stack()
        stack.push(node)

        # Take all of the nodes from the left
        while node is not None and node.left is not None:
            stack.push(node.left)
            node = node.left

        # While the stack isnt empty
        while not stack.is_empty():
            node = stack.pop()
            if node is not None:
                visit(node.data)
                # If there are any right nodes
                if node.right is not None:
                    temp_node = node.right
                    stack.push(temp_node)
                    # Get all their left nodes
                    while temp_node.left is not None:
                        stack.push(temp_node.left)
                        temp_node = temp_node.left

    def items_pre_order(self):
        """Return a pre-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree pre-order from root, appending each node's item
            self._traverse_pre_order_recursive(self.root, items.append)
        # Return pre-order list of all items in tree
        return items

    def _traverse_pre_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node is None:
            return

        # TODO: Visit this node's data with given function
        visit(node.data)
        # TODO: Traverse left subtree, if it exists
        self._traverse_pre_order_recursive(node.left, visit)
        # TODO: Traverse right subtree, if it exists
        self._traverse_pre_order_recursive(node.right, visit)

    def _traverse_pre_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative pre-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse pre-order without using recursion (stretch challenge)
        stack = Stack()
        stack.push(node)

        while not stack.is_empty():
            node = stack.pop()
            if node is not None:
                visit(node.data)
                if node is not None:
                    stack.push(node.right)
                if node is not None:
                    stack.push(node.left)

    def items_post_order(self):
        """Return a post-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree post-order from root, appending each node's item
            self._traverse_post_order_recursive(self.root, items.append)
        # Return post-order list of all items in tree
        return items

    def _traverse_post_order_recursive(self, node, visit):
        """Traverse this binary tree with recursive post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        if node is None:
            return

        # TODO: Traverse left subtree, if it exists
        self._traverse_post_order_recursive(node.left, visit)
        # TODO: Traverse right subtree, if it exists
        self._traverse_post_order_recursive(node.right, visit)
        # TODO: Visit this node's data with given function
        visit(node.data)

    def _traverse_post_order_iterative(self, node, visit):
        """Traverse this binary tree with iterative post-order traversal (DFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Traverse post-order without using recursion (stretch challenge)
        if node is None:
            return

        stack = Stack()
        stack.push(node)

        already_seen = set()

        while not stack.is_empty():
            node = stack.pop()
            if node not in already_seen:
                if node.right is not None and node.left is not None:
                    stack.push(node)
                    already_seen.add(node)
                    if node.right is not None:
                        stack.push(node.right)
                    if node.left is not None:
                        stack.push(node.left)
                else:
                    visit(node.data)
            else:
                visit(node.data)

    def items_level_order(self):
        """Return a level-order list of all items in this binary search tree."""
        items = []
        if not self.is_empty():
            # Traverse tree level-order from root, appending each node's item
            self._traverse_level_order_iterative(self.root, items.append)
        # Return level-order list of all items in tree
        return items

    def _traverse_level_order_iterative(self, start_node, visit):
        """Traverse this binary tree with iterative level-order traversal (BFS).
        Start at the given node and visit each node with the given function.
        TODO: Running time: ??? Why and under what conditions?
        TODO: Memory usage: ??? Why and under what conditions?"""
        # TODO: Create queue to store nodes not yet traversed in level-order
        queue = Queue()
        # TODO: Enqueue given starting node
        queue.enqueue(start_node)
        # TODO: Loop until queue is empty
        while (not queue.is_empty()):
            # TODO: Dequeue node at front of queue
            node = queue.dequeue()
            # TODO: Visit this node's data with given function
            visit(node.data)
            # TODO: Enqueue this node's left child, if it exists
            if (node.left is not None):
                queue.enqueue(node.left)
            # TODO: Enqueue this node's right child, if it exists
            if (node.right is not None):
                queue.enqueue(node.right)


def test_binary_search_tree():
    # Create a complete binary search tree of 3, 7, or 15 items in level-order
    # items = [2, 1, 3]
    items = [4, 2, 6, 1, 3, 5, 7]
    # items = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    print('items: {}'.format(items))

    tree = BinarySearchTree()
    print('tree: {}'.format(tree))
    print('root: {}'.format(tree.root))

    print('\nInserting items:')
    for item in items:
        tree.insert(item)
        print('insert({}), size: {}'.format(item, tree.size))
    print('root: {}'.format(tree.root))

    print('\nSearching for items:')
    for item in items:
        result = tree.search(item)
        print('search({}): {}'.format(item, result))
    item = 123
    result = tree.search(item)
    print('search({}): {}'.format(item, result))

    print('\nTraversing items:')
    print('items in-order:    {}'.format(tree.items_in_order()))
    print('items pre-order:   {}'.format(tree.items_pre_order()))
    print('items post-order:  {}'.format(tree.items_post_order()))
    print('items level-order: {}'.format(tree.items_level_order()))


if __name__ == '__main__':
    test_binary_search_tree()
