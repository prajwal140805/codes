#include <iostream>
using namespace std;

class Student {
    private:
        string name;
        int age;

    public:
        void setDetails(string n, int a);   
        void displayDetails();            
};

 
void Student::setDetails(string n, int a) {
    name = n;
    age = a;
}

void Student::displayDetails() {
    cout << "Student Name: " << name << endl;
    cout << "Student Age: " << age << endl;
}

int main() {
    Student s1;
    s1.setDetails("John", 19);
    s1.displayDetails();

    return 0;
}
