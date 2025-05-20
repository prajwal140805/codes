#include <iostream>
#include <string>
using namespace std;
class Student
{private:
    int rollNumber;
    string name;
    static int studentCount;  
public: 
    Student(string name ,int r){rollNumber = r;this->name =name;studentCount++;  }  
    static void showStudentCount(){cout << "Total students: " << studentCount << endl;}
    void display(){cout << "Student Roll No: " << rollNumber << "\t"<<"Student Name:"<<name<< endl;}
}; 
int Student::studentCount = 0;
int main()
{   Student s1("Jhon",101);
    Student s2("Prajwal",102);
    Student s3("Riya",103);
    s1.display();
    s2.display();
    s3.display(); 
    Student::showStudentCount();
    return 0;}
