from hashtable import HashTable


class HashSet(object):

    def __init__(self, elements=None):
        self.hashset = HashTable()
        self.size = 0

        if elements is not None:
            for element in elements:
                self.add(element)

    def __iter__(self):
        pass

    def all_entries(self):
        pass

    def contains(self, key):
        pass

    def length(self):
        pass

    def add(self, element):
        pass

    def remove(self, element):
        pass

    def union(self, set):
        pass

    def intersection(self, set):
        pass

    def difference(self, set):
        pass

    def is_subset(self, set):
        pass

    def is_superset(self, set):
        pass
