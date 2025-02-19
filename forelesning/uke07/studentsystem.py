from abc import ABC, abstractmethod

class MyDatastructure(ABC):

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_element(self, new_element):
        pass

    @abstractmethod
    def remove_element(self):
        pass

    @abstractmethod
    def print_all(self):
        pass

    @abstractmethod
    def to_list(self):
        pass

class Stack(MyDatastructure):

    def __init__(self):
        self._elements = []

    def add_element(self, new_element):
        self._elements.append(new_element)

    def remove_element(self):
        return self._elements.pop()
    
    def print_all(self):
        for elem in self._elements:
            print(elem)

    def to_list(self):
        return self._elements
    
    def __str__(self):
        return self._elements.__str__()

class Queue(MyDatastructure):

    class Node:

        def __init__(self, data):
            self.data = data
            self.next = None

    def __init__(self):
        self._first = None

    def add_element(self, data):
        if self._first == None:
            self._first = Queue.Node(data)
        else:
            iternode = self._first
            while iternode.next != None:
                iternode = iternode.next
            iternode.next = Queue.Node(data)

    def remove_element(self):
        data = self._first.data
        self._first = self._first.next
        return data
    
    def print_all(self):
        if not self._first:
            return
        iternode = self._first
        while iternode != None:
            print(iternode.data)
            iternode = iternode.next

    def to_list(self):
        all_elements = []
        iternode = self.first
        while iternode != None:
            all_elements.append(iternode.data)
            iternode = iternode.next
        return all_elements


class Studentsystem:

    def __init__(self):
        self.studenter = Stack()

    def legg_til_student(self, navn):
        self.studenter.add_element(navn)

    def fjern_siste_student(self):
        return self.studenter.remove_element()

    def print_alle_studenter(self):
        self.studenter.print_all()


if __name__ == "__main__":
    s = Stack()
    q = Queue()

    s.add_element("Arne")
    q.add_element("Berit")

    if isinstance(q, MyDatastructure):
        print("Current data:")
        q.print_all()
    else:
        raise TypeError("Expected a MyDatastructure lol")
    