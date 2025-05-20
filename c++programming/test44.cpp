#include <iostream>
using namespace std;
class A {
public:
    void display() {
        cout << "Display from A" << endl;
    }
};

class B {
public:
    void display() {
        cout << "Display from B" << endl;
    }
};

class C : public A, public B {
public:
    void show() {
        A::display();  // No confusion now
        B::display();  // You told C++ exactly what you want
    }

};
int main() {
        C obj;
        obj.show();
        return 0;
    }
