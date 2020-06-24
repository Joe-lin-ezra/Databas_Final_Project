from read import readcsv
from bplustree import BplusTree

if __name__ == '__main__':
    keys = readcsv()
    tree = BplusTree(3)
    for i in range(5):
        tree.insert(i+1)
    tree.print()