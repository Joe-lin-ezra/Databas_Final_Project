from read import readcsv
from bplustree import BplusTree
from Test import treetest

if __name__ == '__main__':
    keys = readcsv()
    tree = BplusTree(3)
    test = treetest(5)
    for i in range(27):
        print(keys[i])
        test.insert(keys[i])
    test.print()