#include "myDatastructure.hpp"
#include <iostream>

int main() {
    Stack s = Stack();
    s.addElement("Hello");
    s.addElement("Heisann hehe");
    std::cout << s.removeElement() << std::endl;
    return 0;
}