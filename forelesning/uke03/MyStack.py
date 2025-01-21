from MyLL import MyLinkedList

class MyStack(MyLinkedList):

    def __init__(self):
        super().__init__()

    def push(self, data):
        super().append(data)

    def peek(self):
        return super().get(self.length - 1)
    
    def pop(self):
        data = self.get(self.length - 1)
        super().remove(self.length - 1)
        return data
    
    def remove(self, index):
        raise NotImplementedError
    
    def get(self, index):
        raise NotImplementedError
    
    def set(self, index, data):
        raise NotImplementedError
    

if __name__ == "__main__":
    stack = MyStack()
    for i in range(1, 21, 2):
        stack.push(i)
    print(stack)
    print(stack.peek())
    print(stack.pop())
    print(stack)