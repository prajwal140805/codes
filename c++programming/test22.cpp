#include <iostream>
using namespace std;

class Employee {
public:
    int EID;
    string EmpName;

    void display( ) {
        cout << "Employee ID: " << EID << endl;
        cout << "Employee Name: " << EmpName << endl;
    }
};

int main() { 
    Employee emp;   
    emp.EID = 101;
    emp.EmpName = "Prajwal Kumar";   
    
    emp.display();
    return 0;
}
