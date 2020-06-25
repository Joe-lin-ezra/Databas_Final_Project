import copy

class BplusTree():
    def __init__(self, D):
        self.root = ExternalNode()
        self.leaf = None
        self.D = D

    def insert(self, data):
        pass

    def print(self):
        pass


    def delete(self):
        pass

    def splite(self, data):
        pass

    def search(self):
        pass


class InternalNode():
    def __init__(self):
        self.leaf = []
        self.ptr = []


class ExternalNode():
    def __init__(self):
        self.data = []
        self.ptr = None
