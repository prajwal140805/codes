#include <iostream>
using namespace std;

class Employee {
public:
    int id=100; // instance variable
    
    void setId(int id) {
       this-> id = id; // Using 'this' to differentiate between parameter and instance variable
    }

    void display() {
        cout << "Employee ID: " << id << endl;
    }
};

int main() {
    Employee e1;
    e1.setId(101);
    e1.display();
    return 0;
}
