#include <iostream>
using namespace std;

int main()
{
    string name;
    do
    {
        cout << "enter your name:";
        getline(cin, name);
    } while (name.empty());

    cout << "welcome " << name << ", this is the world of demons😎💀";
    return 0;
}