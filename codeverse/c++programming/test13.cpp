#include <iostream>
using namespace std;

class employee
{
private:
    int a, b, c;

public:
    int d, f;
    void setData(int a1, int b1, int c1);
    void getdata()
    {
        cout << "The value of a is " << a << endl;
        cout << "The value of b is " << b << endl;
        cout << "The value of c is " << c << endl;
        cout << "The value of d is " << d << endl;
        cout << "The value of e is " << f << endl;
    }
};
void employee::setData(int a1, int b1, int c1)
{
    a = a1;
    b = b1;
    c = c1;
}
int main()
{
    employee emp;
    emp.setData(1, 2, 3);
    emp.d = 4;
    emp.f = 5;
    emp.getdata();

    return 0;
}