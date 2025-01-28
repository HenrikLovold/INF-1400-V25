
class MyLinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

        def insert(self, data):
            if self.next == None:
                self.next = MyLinkedList.Node(data)
            else:
                self.next.insert(data)
        
        def count_up(self, n):
            if self.next == None:
                return n+1
            else:
                return self.next.count_up(n+1)
            
        def contains(self, data):
            if self.data == data:
                return True
            if self.next == None:
                return False
            return self.next.contains(data)
        
        def remove(self, data):
            if self.next.data == data:
                self.next = self.next.next
            else:
                self.next.remove(data)

    def __init__(self):
        self.first = None
        self.iter_node = None
        
    def insert(self, data):
        if self.first == None:
            self.first = MyLinkedList.Node(data)
        else:
            self.first.insert(data)

    def contains(self, data):
        if self.first == None:
            return False
        return self.first.contains(data)
    
    def remove(self, data):
        if not self.contains(data):
            raise RuntimeError("Attempted to remove non-existing data")
        if self.first.data == data:
            self.first = self.first.next
        else:
            print("Removing recursively")
            self.first.remove(data)

    def __len__(self):
        if self.first == None:
            return 0
        return self.first.count_up(0)
    
    def __iter__(self):
        self.iter_node = self.first
        return self
    
    def __next__(self):
        if self.iter_node == None:
            raise StopIteration
        data = self.iter_node.data
        self.iter_node = self.iter_node.next
        return data
    
    def __add__(self, other_list):
        new_ll = MyLinkedList()
        for element in self:
            new_ll.insert(element)
        for element in other_list:
            new_ll.insert(element)
        return new_ll
    
    def __str__(self):
        info = ""
        for element in self:
            info += str(element) + " "
        return info
    

if __name__ == "__main__":
    ll1 = MyLinkedList()
    ll1.insert(2)
    ll1.insert(1)
    ll1.insert(6)

    ll2 = MyLinkedList()
    ll2.insert(8)
    ll2.insert(4)

    ll3 = ll1 + ll2
    print(ll3)
    ll3.remove(6)
    print(ll3)

