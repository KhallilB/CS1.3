from hashtable import HashTable


class HashSet(object):

    def __init__(self, elements=None):
        self.hashset = HashTable()
        self.size = 0

        if elements is not None:
            for element in elements:
                self.add(element)

    def __iter__(self):
        """Allows all of the items in the the set to
        be iterable, allowing them to be looped over.
         Time complexity: O(n) where n is all of the
         items in the set"""
        for item in self.all_entries():
            yield item

    def __length__(self):
        """Returns a count of all of the items in the set.
        Time Complexity of O(1), just returns a stored
        variable"""
        return self.size

    def all_entries(self):
        """Returns all keys in the entire set.Time complexity:
         Uses the key function from Hashtable class which is O(n). 
         O(n) where n is the amount of items in the set."""
        return self.hashset.keys()

    def contains(self, key):
        """Returns true or false if a key exists in a set. 
        Time complextity: O(b) where b is the amount of items 
        in a bucket."""
        return self.hashset.contains(key)

    def add(self, key_value):
        """Adds a key value pair to a set."""
        self.size += 1
        return self.hashset.set(key_value, key_value)

    def remove(self, key_value):
        """Removes a key value pair from a set."""
        self.size -= 1
        return self.hashset.delete(key_value)

    def union(self, sec_set):
        """Returns a new set with all elements from our set and 
        the second set. Time complexity is O(n) where n is the amount 
        of elements in the set an the second set and space complexity 
        is also O(n) because we add that many items."""
        union = sec_set
        for key_value in self:
            union.add(key_value)
        return union

    def intersection(self, sec_set):
        """Returns a new set with all elements that are in both our 
        set and the second set. Time complexity is O(n) where n is min amount
        of items in our set and the second set. The space complexity is also 
        O(n) because we add that many items."""
        intersection = HashSet()

        if sec_set.size < self.size:
            smaller = sec_set
            larger = self
        else:
            smaller = self
            larger = sec_set
        for key_value in smaller:
            if larger.contains(key_value):
                intersection.add(key_value)
        return intersection

    def difference(self, sec_set):
        """Returns a new set with all elements that are in our set but not in 
        the second set. Time complexity is O(n) where n is the number 
        of items in our set and space complexity is also O(n) 
        because we add that many items."""
        difference = self
        intersection = self.intersection(sec_set)

        for item in intersection:
            difference.remove(item)
        return difference

    def is_subset(self, sec_set):
        """Returns true if our entire set is in the second set. Time 
        complexity is O(n) where n is the number of items in our set
        and space complexity is also O(n) because we don't add any
        new variables."""
        for key_value in self:
            if key_value not in sec_set:
                return False
        return True

    def is_superset(self, sec_set):
        """Returns true if all items in the second set are in our set. 
        Time complexity is O(n) where n is the number of items in the
        second set and space complexity is also O(1) because we 
        don't add any new variables."""
        for key_value in sec_set:
            if key_value not in self:
                return False
        return True
