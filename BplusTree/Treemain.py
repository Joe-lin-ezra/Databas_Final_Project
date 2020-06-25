from read import readcsv
from bplustree import BplusTree
from Test import treetest

if __name__ == '__main__':
    keys = readcsv()
    tree = BplusTree(3)
    test = treetest(3)
    for i in range(3):
        test.insert(i+1)
    test.print()