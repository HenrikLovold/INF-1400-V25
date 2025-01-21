
class MyLinkedList:

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0
        self.iternumber = 0

    def append(self, data):
        if self.first == None:
            self.first = MyLinkedList.Node(data)
            self.last = self.first
        else:
            self.last.next = MyLinkedList.Node(data)
            self.last = self.last.next
        self.length += 1

    def get(self, index):
        if index >= self.length:
            raise IndexError("Attempted to get an object outside the range")
        it = self.first
        for i in range(index):
            it = it.next
        return it.data

    def set(self, index, new_data):
        if index >= self.length:
            raise IndexError("Attempted to set an object outside the range")
        it = self.first
        for i in range(index):
            it = it.next
        it.data = new_data

    def remove(self, index):
        if index >= self.length:
            raise IndexError("Attempted to set an object outside the range")
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            it = self.first
            for i in range(index-1):
                it = it.next
            it.next = it.next.next
            if index == self.length - 1:
                self.last = it.next
        self.length -= 1

    def __getitem__(self, index):
        return self.get(index)
    
    def __setitem__(self, index, data):
        self.set(index, data)

    def __iter__(self):
        self.iternumber = 0
        return self

    def __next__(self):
        if self.iternumber == self.length:
            raise StopIteration
        next_data = self.get(self.iternumber)
        self.iternumber += 1
        return next_data

    def __str__(self):
        info = "{["
        it = self.first
        while it != None:
            info += " " + str(it.data) + " ->"
            it = it.next
        info = info[:-2]
        info += "]}"
        return info
    

if __name__ == "__main__":
    ll = MyLinkedList()
    for i in range(0, 20, 2):
        ll.append(i)
    
    print("Første print:")
    for tall in ll:
        print(tall)

    print("Andre print:")
    for tall in ll:
        print(tall)