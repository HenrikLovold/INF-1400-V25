from MyLL import MyLinkedList

class CompStack:

    def __init__(self):
        self.stack = MyLinkedList()

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        data = self.stack.get(self.stack.length-1)
        self.stack.remove(self.stack.length-1)
        return data
    
    def peek(self):
        return self.stack.get(self.stack.length-1)
    
    def __str__(self):
        return str(self.stack)
    
if __name__ == "__main__":
    stk = CompStack()
    for i in range(0, 10):
        stk.push(i)

    print(stk)
    print(stk.peek())
    print(stk.pop())
    print(stk)