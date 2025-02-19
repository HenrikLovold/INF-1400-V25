#include "myDatastructure.hpp"
#include <iostream>
#include <vector>

Stack::Stack() {
    this->elements = new std::vector<std::string>();
}

void Stack::addElement(std::string data) {
    this->elements->push_back(data);
}

std::string Stack::removeElement() {
    if (this->elements->empty()) {
        return nullptr;
    }
    std::string toReturn = this->elements->at(this->elements->size()-1);
    this->elements->pop_back();
    return toReturn;
}

void Stack::printAll() {
    for (int i = 0; i < this->elements->size(); i++) {
        std::cout << this->elements->at(i) << std::endl;
    }
}