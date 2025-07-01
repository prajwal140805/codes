#include <iostream>
using namespace std;

class Student {
public:
    int rollNo;
    string name;

    void display();  // Function declaration inside class
};

// Function definition outside the class using scope resolution operator
void Student::display() {
    cout << "Roll Number: " << rollNo << endl;
    cout << "Name: " << name << endl;
}

int main() {
    Student s1;

    s1.rollNo = 149;
    s1.name = "Prajwal Kumar";

    s1.display();  // Accessing the function

    return 0;
}
