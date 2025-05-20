#include <iostream>
using namespace std;

class Animal {
public:
    virtual void sound() {
        cout << "Animal sound" << endl;
    }
};

class Dog : public Animal {
public:
    void sound() override {
        cout << "Dog barks" << endl;
    }
};

int main() {
    Animal *a;
    Dog d;

    a = &d;
    a->sound();  // Outputs: Dog barks

    return 0;
}
/* Simple Explanation:
virtual in base class ➝ tells C++ that function can be overridden.
override in derived class ➝ confirms you're overriding it.
We use a base class pointer (Animal* a) pointing to a Dog object.
Even though the pointer is of type Animal, it calls the Dog version of the function → that's runtime polymorphism.*/