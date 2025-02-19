#pragma once

#include <iostream>
#include <vector>

class Stack {
    private:
        std::vector<std::string> *elements;
    public:
        Stack();
        void addElement(std::string data);
        std::string removeElement();
        void printAll();
};
