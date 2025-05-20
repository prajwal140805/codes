#include <iostream>
using namespace std;

int main()
{
    string name;
    int age;
    cout << "enter your full name:";
    getline(cin, name);
    cout << '\n';
    cout << "enter your age:";
    cin >> age;
    cout << '\n';
    cout << "Hello " << name << " you are " << age << " years old.";
    return 0;
}