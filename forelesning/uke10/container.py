import abc
import random

class Container(abc.ABC):

    def __init__(self):
        pass

    @abc.abstractmethod
    def insert(self, object):
        pass

    @abc.abstractmethod
    def contains(self, object):
        pass

    @abc.abstractmethod
    def print_all(self):
        pass

class SingleLinkedList(Container):

    class Node:

        def __init__(self, element):
            self.data = element
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None

    def insert(self, object):
        if self.first == None:
            self.first = SingleLinkedList.Node(object)
            self.last = self.first
        else:
            self.last.next = SingleLinkedList.Node(object)
            self.last = self.last.next

    def contains(self, object):
        iternode = self.first
        while iternode != None:
            if iternode.data == object:
                return True
            iternode = iternode.next
        return False

    def print_all(self):
        iternode = self.first
        while iternode != None:
            print(iternode.data)
            iternode = iternode.next

class BinarySearchTree(Container):

    class Node:

        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

        def insert(self, data):
            if data < self.data:
                if self.left == None:
                    self.left = BinarySearchTree.Node(data)
                else:
                    self.left.insert(data)
            else:
                if self.right == None:
                    self.right = BinarySearchTree.Node(data)
                else:
                    self.right.insert(data)

        def contains(self, data):
            if self.data == data:
                return True
            if data < self.data:
                if self.left != None:
                    return self.left.contains(data)
                return False
            else:
                if self.right != None:
                    return self.right.contains(data)
                return False
            
        def print_node(self):
            if self.left != None:
                self.left.print_node()
            print(self.data)
            if self.right != None:
                self.right.print_node()


    def __init__(self):
        self.root = None

    def insert(self, object):
        if self.root == None:
            self.root = BinarySearchTree.Node(object)
        else:
            self.root.insert(object)
            
    def contains(self, object):
        if self.root == None:
            return False
        return self.root.contains(object)

    def print_all(self):
        if self.root != None:
            self.root.print_node()


if __name__ == "__main__":
    bst = BinarySearchTree()
    for _ in range(15):
        bst.insert(random.randint(0, 100))
    bst.print_all()