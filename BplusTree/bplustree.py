import copy

class BplusTree():
    def __init__(self, D):
        self.root = ExternalNode()
        self.leaf = None
        self.D = D

    def insert(self, data):
        #data = int(data[2:6])
        ptr = self.searchleaf(self.root,data)
        ptr.data.append(data)
        ptr.data.sort()
        if len(ptr.data) == self.D:
            TorF, newNode = self.updata(self.root,data)
            if TorF:
                if type(self.root) == ExternalNode:
                    self.root = newNode
                    self.leaf = newNode.ptr[0]
                else:
                    if len(self.root.leaf) == self.D:
                        self.root.leaf.sort()
                        left = InternalNode()
                        Right = InternalNode()
                        left.leaf = self.root.leaf[:int(self.D/2)]
                        Right.leaf = self.root.leaf[int(self.D / 2)+1:]
                        left.ptr = self.root.ptr[:int(self.D / 2)+1]
                        Right.ptr = self.root.ptr[int(self.D / 2) + 1:]
                        self.root.leaf.clear()
                        self.root.leaf = newNode.leaf
                        self.root.ptr.clear()
                        self.root.ptr.append(left)
                        self.root.ptr.append(Right)

    def print(self):
        print(self.root.leaf,"root")
        print(self.root.ptr[0].leaf, "leaf")
        print(self.root.ptr[0].ptr[0].data, "data")
        print(self.root.ptr[0].ptr[1].data, "data")
        print(self.root.ptr[0].ptr[2].data, "data")
        print(self.root.ptr[1].leaf, "leaf")
        print(self.root.ptr[1].ptr[0].data, "data")
        print(self.root.ptr[1].ptr[1].data, "data")
        print(self.root.ptr[1].ptr[2].data, "data")
        print(self.root.ptr[2].leaf, "leaf")
        print(self.root.ptr[2].ptr[0].data, "data")
        print(self.root.ptr[2].ptr[1].data, "data")
        print(self.root.ptr[2].ptr[2].data, "data")
        print(self.leaf.data)
        print(self.leaf.ptr.data)
        print(self.leaf.ptr.ptr.data)
        print(self.leaf.ptr.ptr.ptr.data)
        print(self.leaf.ptr.ptr.ptr.ptr.data)
        print(self.leaf.ptr.ptr.ptr.ptr.ptr.data)
        print(self.leaf.ptr.ptr.ptr.ptr.ptr.ptr.data)
        #for d in range(len(self.root.ptr)):
        #    print(self.root.ptr[d].leaf,"leaf,d",d)
        #    for y in range(len(self.root.ptr[d].ptr)):
        #        print(self.root.ptr[d].ptr[y].leaf,"leaf,y",y)
        #        for j in range(len(self.root.ptr[d].ptr[y].ptr)):
        #            print(self.root.ptr[d].ptr[y].ptr[j].data, "data,j", j)


    def delete(self):
        pass

    def updata(self, ptr, data):
        global flag
        flag = 0
        if type(ptr) == ExternalNode:
            tmp = InternalNode()
            Right = ExternalNode()
            tmp.leaf.append(ptr.data[int(self.D / 2)])
            Right.data = ptr.data[int(self.D / 2):]
            ptr.data = ptr.data[:int(self.D / 2)]
            tmp.ptr.append(ptr)
            tmp.ptr.append(Right)
            if ptr.ptr:
                tmp1 = ptr.ptr
                Right.ptr = tmp1
                ptr.ptr = Right
            else:
                ptr.ptr = Right
            return True, tmp
        else:
            if len(ptr.leaf) > 1:
                if ptr.leaf[0] < data < ptr.leaf[-1]:
                    for d in range(len(ptr.leaf) - 1):
                        if data > ptr.leaf[d] and data > ptr.leaf[d + 1]:
                            continue
                        else:
                            TorF, newNode = self.updata(ptr.ptr[d + 1], data)
                            flag = 1
                            if TorF:
                                for d in range(len((ptr.ptr))):
                                    if ptr.ptr[d] == newNode.ptr[0]:
                                        ptr.ptr.insert((d + 1), newNode.ptr[1])
                                        ptr.leaf.insert((d + 1), newNode.leaf[0])
                                if len(ptr.leaf) == self.D:
                                    return True, newNode
                            return False, newNode
                elif data < ptr.leaf[0]:
                    TorF, newNode = self.updata(ptr.ptr[0], data)
                    if TorF:
                        ptr.leaf += newNode.leaf
                        ptr.leaf.sort()
                        ptr.ptr.pop(0)
                        ptr.ptr = newNode.ptr + ptr.ptr
                        if len(ptr.leaf) == self.D:
                            ptr.leaf.sort()
                            left = InternalNode()
                            Right = InternalNode()
                            left.leaf = ptr.leaf[:int(self.D / 2)]
                            Right.leaf = ptr.leaf[int(self.D / 2) + 1:]
                            left.ptr = ptr.ptr[:int(self.D / 2) + 1]
                            Right.ptr = ptr.ptr[int(self.D / 2) + 1:]
                            newNode.leaf.pop()
                            newNode.leaf.append(ptr.leaf[int(self.D / 2)])
                            ptr.leaf.clear()
                            ptr.leaf = newNode.leaf
                            ptr.ptr.clear()
                            ptr.ptr.append(left)
                            ptr.ptr.append(Right)
                            return True, ptr
                    return False, newNode
                else:
                    TorF, newNode = self.updata(ptr.ptr[-1], data)
                    flag = 2
                    if TorF:
                        ptr.leaf += newNode.leaf
                        ptr.leaf.sort()
                        ptr.ptr.pop()
                        ptr.ptr += newNode.ptr
                        if len(ptr.leaf) == self.D:
                            tmp = InternalNode()
                            Right = InternalNode()
                            tmp.leaf.append(ptr.leaf[int(self.D / 2)])
                            Right.leaf = ptr.leaf[int(self.D / 2):]
                            ptr.leaf = ptr.leaf[:int(self.D / 2)]
                            tmp.ptr.append(ptr)
                            tmp.ptr.append(Right)
                            return True, tmp
                    return False, newNode
            else:
                if ptr.leaf[0] < data:
                    TorF, newNode = self.updata(ptr.ptr[1], data)
                    flag = 2
                    if TorF:
                        ptr.leaf += newNode.leaf
                        ptr.leaf.sort()
                        ptr.ptr.pop()
                        ptr.ptr += newNode.ptr
                        if len(ptr.leaf) == self.D:
                            return True, newNode
                    return False, newNode
                else:
                    TorF, newNode = self.updata(ptr.ptr[0], data)
                    if TorF:
                        ptr.leaf += newNode.leaf
                        ptr.leaf.sort()
                        ptr.ptr.pop(0)
                        ptr.ptr = newNode.ptr + ptr.ptr
                        if len(ptr.leaf) == self.D:
                            return True, newNode
                    return False, newNode

    def search(self):
        pass

    def searchleaf(self,ptr,data):
        if type(ptr) == ExternalNode:
            return ptr
        else:
            if len(ptr.leaf) > 1:
                if ptr.leaf[0] < data < ptr.leaf[-1]:
                    for d in range(len(ptr.leaf) - 1):
                        if data > ptr.leaf[d] and data > ptr.leaf[d + 1]:
                            continue
                        else:
                            return self.searchleaf(ptr.ptr[d+1],data)
                elif data < ptr.leaf[0]:
                    return self.searchleaf(ptr.ptr[0],data)
                else:
                    return self.searchleaf(ptr.ptr[-1],data)
            else:
                if ptr.leaf[0] < data:
                    return self.searchleaf(ptr.ptr[1],data)
                else:
                    return self.searchleaf(ptr.ptr[0], data)

class InternalNode():
    def __init__(self):
        self.leaf = []
        self.ptr = []


class ExternalNode():
    def __init__(self):
        self.data = []
        self.ptr = None
