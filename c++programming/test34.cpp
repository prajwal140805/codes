/*Design a class called Person with member variables for name and age. Derive classes Student
 and Teacher from Person. Implement member functions to display deta*/
#include<iostream>
 using namespace std;
 class Person {
 protected:
 string name;
 int age;
 public:  
    Person(string n, int a) {  
        name = n;  
        age = a;  
    }  
    void displayDetails() {  
        cout << "Name: " << name << ", Age: " << age << endl;  
    }
 };
 class Student : public Person {
 public:
 Student(string n, int a) : Person(n, a) {}  
 void displayStudent() {  
        displayDetails();  
        cout << "Role: Student\n";  
    }
 };
 class Teacher : public Person {
 public:
    Teacher(string n, int a) : Person(n, a) {}
 
 void displayTeacher() {  
        displayDetails();  
        cout << "Role: Teacher\n";  
    }
 };
 int main() {
 Student s1("Navnit Nayan", 19);
 Teacher t1("Tushar Varshney", 18);
 s1.displayStudent();  
t1.displayTeacher();  
return 0;
 }