
#include <iostream>
using namespace std;

class Students
{
public:
    int roll_no;
    string religion;
    string f_name;
    int standard;
    int age;
     

    void setData(int r, string rel, string x, int y, int z); 
    void getData()
    {
        cout << "The roll number of student is " << roll_no << endl;
        cout << "The religion of student is " << religion << endl;
        cout << "The Father's name of student is " << f_name << endl;
        cout << "The standard of student is " << standard << endl;
        cout << "The age of student is " << age << endl;
    }
};

void Students ::setData(int r, string rel, string x, int y , int z)
{ 
    roll_no = r;
    religion = rel;
    f_name = x;
    standard = y;
    age =  z;
   
}

int main()
{
    Students prajwal;
//  prajwal.setData(36, "religion", "father name", 13, 19);
    prajwal.setData(36, "Hindu", "prashant", 13 ,19);
    prajwal.getData();
    return 0;
}