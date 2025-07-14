#include <iostream>
#include <fstream>
using namespace std;

struct Student {
    int roll_no;
    char name[20];
};

int main() { 
   Student  s = {36, "Prashant"};
ofstream wf("student.dat", ios::binary);
wf.write((char*)&s, sizeof(s)); // 🔥 writes all data as binary
wf.close();

    // Open binary file for reading
    ifstream rf("student.dat", ios::binary);

    if (!rf) {
        cout << "❌ Could not open file!" << endl;
        return 1;
    }

    // Read from file
    rf.read((char*)&s, sizeof(s));
    rf.close();

    // Show the data
    cout << "Roll No: " << s.roll_no << endl;
    cout << "Name: " << s.name << endl;

    return 0;
}
