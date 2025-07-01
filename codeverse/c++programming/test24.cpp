#include <iostream>
#include <string>
using namespace std;

class Student
{
    string name;
    int roll_number;
    string branch;
public:
    void inputDetails(string studentName, int studentRollNumber, string studentBranch)
    {
        name = studentName;
        roll_number = studentRollNumber;
        branch = studentBranch;
    }
    void display()
    {
        cout << "Student Details:" << endl;
        cout << "Name: " << name << endl;
        cout << "Roll Number: " << roll_number << endl;
        cout << "Branch: " << branch << endl;
    }
};

int main()
{

    Student student1;

    student1.inputDetails("Prajwal Kumar", 149, "Electronics and Communication");

    student1.display();

    return 0;
}
